from django.contrib import admin
from .models import Filter


class FilterAdmin(admin.ModelAdmin):
    list_filter = ['types']


admin.site.register(Filter, FilterAdmin)
