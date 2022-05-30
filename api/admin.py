from django.contrib import admin
from .models import *


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone']
    search_fields = ['name']


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ['store_name']
    search_fields = ['store_name']


@admin.register(StoreVisitLog)
class StoreVisitLogAdmin(admin.ModelAdmin):
    list_display = ['visited_at']
    search_fields = ['store__store_name', 'store__employee__name']

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False
