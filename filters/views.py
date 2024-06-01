from django.db.models import Count, Prefetch
from django.http import JsonResponse
from django.template.loader import render_to_string

from base import config
from interests.models import Interest

from .models import Filter


def filter_interests(param_dict):
    interestList = param_dict["interestList"]
    filters = [
        "world",
        "country",
        "region",
        "local",
        "city",
        "facility",
        "service",
        "rating",
        "sp1",
        "sp2",
        "sp3",
    ]

    for filter_name in filters:
        if param_dict[filter_name]:
            interestList = interestList.filter(
                interest_filter__in=param_dict[filter_name]
            )

    return interestList.filter(display=True).distinct()


def filter_data(request):
    # page_type = cache.get('page_type')
    page_type = request.GET.get("pageType")
    defaultInterests = request.GET.get("defaultInterests")
    defaultInterests = defaultInterests.strip("][").split(", ")

    initial_dict = {
        # "interestList": cache.get('defaultInterests'),
        "interestList": Interest.objects.filter(id__in=defaultInterests),
        "world": request.GET.getlist("world[]"),
        "country": request.GET.getlist("country[]"),
        "region": request.GET.getlist("region[]"),
        "local": request.GET.getlist("local[]"),
        "city": request.GET.getlist("city[]"),
        "facility": request.GET.getlist("facility[]"),
        "service": request.GET.getlist("service[]"),
        "rating": request.GET.getlist("rating[]"),
        "sp1": request.GET.getlist("sp1[]"),
        "sp2": request.GET.getlist("sp2[]"),
        "sp3": request.GET.getlist("sp3[]"),
    }

    interests_qs = filter_interests(initial_dict).order_by("-rating")
    total_interests = interests_qs.count()
    interests_id = list(interests_qs.values_list("id", flat=True))

    # Pagination
    # per_page = int(cache.get('perPage'))
    per_page = int(request.GET.get("perPage"))
    num_pages = int(total_interests / per_page) + (total_interests % per_page > 0)
    current_page = 1
    page_range = [i for i in range(1, num_pages + 1)]

    interests = interests_qs[
        ((current_page - 1) * per_page) : (current_page * per_page)
    ]

    filter_types = [
        "RATING",
        "WORLD",
        "COUNTRY",
        "REGION",
        "LOCAL",
        "CITY",
        "SP1",
        "SP2",
        "SP3",
        "FACILITY",
        "SERVICE",
    ]
    if page_type == "CITY":
        filter_types = [
            i for i in filter_types if i not in ("WORLD", "COUNTRY", "REGION", "LOCAL")
        ]
    elif page_type == "LOCAL":
        filter_types = [
            i for i in filter_types if i not in ("WORLD", "COUNTRY", "REGION")
        ]
    elif page_type == "REGION":
        filter_types = [i for i in filter_types if i not in ("WORLD", "COUNTRY")]
    elif page_type == "COUNTRY":
        filter_types = [i for i in filter_types if i not in ("WORLD")]
    all_filters = (
        Filter.objects.filter(types__in=filter_types)
        .prefetch_related(
            Prefetch("interests", queryset=Interest.objects.filter(display=True))
        )
        .order_by("order", "name")
    )

    filter_dict = {
        filter_type: all_filters.filter(types=filter_type)
        for filter_type in filter_types
    }

    count_list = []
    for filter_type, filters in filter_dict.items():
        for f in filters:
            filtered_interests = [
                interest for interest in f.interests.all() if interest in interests_qs
            ]
            count_list.append(len(filtered_interests))

    count_result = count_list * 2
    print("Here in result set of count")
    print(filter_dict)
    print("Here in result set of count")

    data = render_to_string(
        "ajax/interest_list.html",
        {
            "info1_label": config.LABEL_INFO1,
            "info2_label": config.LABEL_INFO2,
            "info3_label": config.LABEL_INFO3,
            "info4_label": config.LABEL_INFO4,
            "info5_label": config.LABEL_INFO5,
            "page_type": page_type,
            "interests": interests,
            "interests_id": interests_id,
            "per_page": per_page,
            "num_pages": num_pages,
            "current_page": current_page,
            "page_range": page_range,
        },
    )
    return JsonResponse(
        {"data": data, "total_interests": total_interests, "count_result": count_result}
    )


def load_more_data(request):
    page_type = request.GET.get("pageType")
    currentInterests = request.GET.get("currentInterests")
    currentInterests = currentInterests.strip("][").split(", ")

    # interests_qs = cache.get('currentInterests')
    interests_qs = (
        Interest.objects.filter(id__in=currentInterests, display=True)
        .distinct()
        .order_by("-rating")
    )
    total_interests = interests_qs.count()
    interests_id = list(interests_qs.values_list("id", flat=True))

    # Pagination
    # per_page = int(cache.get('perPage'))
    per_page = int(request.GET.get("perPage"))
    num_pages = int(total_interests / per_page) + (total_interests % per_page > 0)
    current_page = int(request.GET.get("currentPage"))
    page_range = [i for i in range(1, num_pages + 1)]

    interests = interests_qs[
        ((current_page - 1) * per_page) : (current_page * per_page)
    ]

    data = render_to_string(
        "ajax/interest_list.html",
        {
            "info1_label": config.LABEL_INFO1,
            "info2_label": config.LABEL_INFO2,
            "info3_label": config.LABEL_INFO3,
            "info4_label": config.LABEL_INFO4,
            "info5_label": config.LABEL_INFO5,
            "page_type": page_type,
            "interests": interests,
            "interests_id": interests_id,
            "per_page": per_page,
            "num_pages": num_pages,
            "current_page": current_page,
            "page_range": page_range,
        },
    )
    return JsonResponse({"data": data, "total_interests": total_interests})
