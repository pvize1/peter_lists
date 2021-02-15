from django.contrib import admin
from django.template.defaultfilters import slugify
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )
    search_fields = ["title", "author"]
    prepopulated_fields = {"slug": ("title",)}
