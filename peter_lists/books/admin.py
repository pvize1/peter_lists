from django.contrib import admin
from .models import Book, Author, BookType, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "type",
        "status",
    ]
    ordering = ["type", "status", "title"]
    prepopulated_fields = {"slug": ("title",)}
    # date_hierarchy = ""
    list_filter = [
        "type__type",
        "status",
        "author__name",
    ]
    search_fields = [
        "title",
        "type__type",
        "status",
        "author__name",
    ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ["name"]


@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ("type",)
    ordering = ["type"]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)
    ordering = ["name"]
