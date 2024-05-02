from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from user.models import LibraryUser


# Register your models here.
@admin.register(LibraryUser)
class  LibraryUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","first_name", "last_name", 'email'),
            },
        ),
    )
