from django.contrib import admin
from .models import Blog, ImageList


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "tag"]
    ordering = ["-date", "title"]
    date_hierarchy = "date"
    list_filter = ["tag"]
    search_fields = ["title", "tag"]

@admin.register(ImageList)
class ImageListAdmin(admin.ModelAdmin):
    pass
