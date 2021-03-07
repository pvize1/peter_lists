from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Book, Author, BookType, Publisher


def make_fiction(modeladmin, request, queryset):
    queryset.update(type=7)


def make_nonfiction(modeladmin, request, queryset):
    queryset.update(type=6)


def make_read(modeladmin, request, queryset):
    queryset.update(status="RD")


def make_reading(modeladmin, request, queryset):
    queryset.update(status="RG")


make_fiction.short_description = "Mark book types as Fiction"
make_nonfiction.short_description = "Mark book types as Non-Fiction"
make_read.short_description = "Mark book status as Completed"
make_reading.short_description = "Mark book status as Reading"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            _("ABOUT"),
            {
                "fields": (
                    ("title", "tag", "slug"),
                    ("subtitle", "author"),
                    "description",
                )
            },
        ),
        (
            _("DETAILS"),
            {
                "fields": (
                    ("publisher", "isbn"),
                    ("type", "status", "form"),
                    ("pages", "rating", "pct_read"),
                )
            },
        ),
    )
    list_display = [
        "title",
        "subtitle",
        "author",
        "publisher",
        "type",
        "status",
    ]
    ordering = [
        "type__type",
        "status",
        "title",
    ]
    prepopulated_fields = {"slug": ("title",)}
    actions = [
        make_fiction,
        make_nonfiction,
        make_read,
        make_reading,
    ]
    # date_hierarchy = ""
    list_filter = [
        "type__type",
        "status",
        "form",
        "author__name",
        "publisher__name",
    ]
    search_fields = [
        "title",
        "subtitle",
        "type__type",
        "status",
        "author__name",
        "publisher__name",
    ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    ordering = ["name"]


@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "type",
    )
    ordering = ["type"]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
    ordering = ["name"]
