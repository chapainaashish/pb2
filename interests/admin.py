from django.contrib import admin
from django import forms
from .models import RegionImage, Region, Interest, TopSliderImage, CoverSliderImage, ReviewAndRating, Comment
from filters.models import Filter
from import_export.admin import ImportExportModelAdmin
from .resources import InterestResource
from base import config
from .forms import InterestAdminForm


class RegionImageInline(admin.TabularInline):
    model = RegionImage


class RegionAdmin(admin.ModelAdmin):
    search_fields = ['name']
    inlines = [RegionImageInline]
    readonly_fields = ('slug', 'id', 'geo_link',)


class TopSliderImageInline(admin.TabularInline):
    model = TopSliderImage


class CoverSliderImageInline(admin.TabularInline):
    model = CoverSliderImage


class FilterInlineForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            # Get the selected filter instance
            instance = kwargs['instance']

            # Check if the instance is saved (editing existing)
            if instance.pk:
                # Filter the available filters based on the selected filter's type
                self.fields['filter'].queryset = Filter.objects.filter(types=instance.filter.types)

class FilterInline(admin.TabularInline):
    model = Filter.interests.through
    form = FilterInlineForm
    extra = 0


class InterestAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    inlines = [TopSliderImageInline, CoverSliderImageInline, FilterInline]
    readonly_fields = ('id', 'add_date', 'mod_date',)
    search_fields = ['name', 'text']
    list_filter = ['display', 'region', 'isvalidated']
    list_display = ('id', 'name', 'add_date', 'mod_date', 'isvalidated',)
    list_display_links = ('id', 'name')
    resource_class = InterestResource
    form = InterestAdminForm

    def has_import_permission(self, request):
        # Only allow superusers to import data
        return request.user.is_superuser

    def has_export_permission(self, request):
        # Only allow superusers to export data
        return request.user.is_superuser

    def get_form(self, request, obj=None, **kwargs):
        form = super(InterestAdmin, self).get_form(request, obj, **kwargs)
        # Only allow superusers to edit user
        if not request.user.is_superuser:
            form.base_fields["user"].disabled = True
        return form


class ReviewAndRatingAdmin(admin.ModelAdmin):
    search_fields = ['title', 'review']
    list_filter = ['approved']


class CommentAdmin(admin.ModelAdmin):
    search_fields = ['title', 'body']
    list_filter = ['approved']


admin.site.register(Region, RegionAdmin)
admin.site.register(Interest, InterestAdmin)
admin.site.register(ReviewAndRating, ReviewAndRatingAdmin)
admin.site.register(Comment, CommentAdmin)
