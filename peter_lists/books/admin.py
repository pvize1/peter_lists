from django.contrib import admin
from django.template.defaultfilters import slugify
from .models import Book, Author, BookType, Publisher


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
    )
    search_fields = ["title", "author"]
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(BookType)
class BookTypeAdmin(admin.ModelAdmin):
    list_display = ("type",)

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name",)
