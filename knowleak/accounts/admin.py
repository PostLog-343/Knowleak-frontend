from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'first_name',)
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    ordering = ('-start_date',)
    list_display = ('email', 'username', 'first_name', 'token',
                    'is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','last_name', 'password','token',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser', 'is_teacher' )})
    )

admin.site.register(User, UserAdminConfig)