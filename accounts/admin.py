from django.contrib import admin
from .models import CustomUser, Region, Institution, Status

# Register your models here.


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_count')
    ordering = ('name',)
    search_fields = ('name',)

    def user_count(self, obj):
        return obj.users_region.count()


@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_count')
    ordering = ('name',)
    search_fields = ('name',)

    def user_count(self, obj):
        return obj.users_institution.count()


@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'user_count')
    ordering = ('name',)
    search_fields = ('name',)

    def user_count(self, obj):
        return obj.users_status.count()


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "username",
                    'status', 'region', 'institution')
    list_per_page = 10
    ordering = ('first_name', 'last_name')
    list_filter = ('status', 'region', 'institution')
