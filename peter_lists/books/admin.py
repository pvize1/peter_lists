from django.contrib import admin
from django.template.defaultfilters import slugify
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ["title"]
    prepopulated_fields = {"slug": ("title",)}

    def slug_title(self):
        return slugify(self.title)
