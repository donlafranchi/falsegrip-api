from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportExportMixin

from .models import AppUser


class AppUserAdmin(ImportExportMixin, UserAdmin):
    ordering = ('first_name',)
    list_filter = ('is_active',)
    list_display = ('username', 'first_name', 'last_name', 'phone', 'is_superuser')
    search_fields = ('username', 'last_name', 'first_name')
    fieldsets = (
        ('User Info', {
            'fields': (
                'username',
                ('first_name', 'last_name'),
                ('email', 'phone',),
                ('weight', 'birthday',),
                'city',
            ),
        }),
        ('Roles', {
            'fields': (
                ('is_active', 'is_superuser'),
                'groups',
                'user_permissions'
            ),
        }),
        ('Other', {
            'fields': (
                ('date_joined', 'last_login'),
            )
        })
    )


admin.site.register(AppUser, AppUserAdmin)
