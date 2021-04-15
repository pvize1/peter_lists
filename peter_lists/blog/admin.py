from django.contrib import admin
from .models import Blog, ImageList


class image_list_inline(admin.TabularInline):
    model = ImageList
    extra = 0


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "tag"]
    ordering = ["-date", "title"]
    date_hierarchy = "date"
    list_filter = ["tag"]
    search_fields = ["title", "tag"]
    inlines = [image_list_inline]


@admin.register(ImageList)
class ImageListAdmin(admin.ModelAdmin):
    ordering = ["order"]
