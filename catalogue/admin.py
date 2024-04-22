from django.contrib import admin

# Register your models here.

from . import models

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'isbn','list_genres']
    list_per_page = 10
    search_fields = ['title','isbn']
    ordering = ['title']

@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['FirstName', 'LastName', 'date_of_birth']


admin.site.register(models.Genre)

