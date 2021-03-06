from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Foodstuff, Ingredient, IngredientList, Recipe, CookBookList


class ingredient_list_inline(admin.TabularInline):
    model = IngredientList
    extra = 1


class cookbook_list_inline(admin.TabularInline):
    model = CookBookList
    extra = 0


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = (
        (_("GENERAL"), {"fields": (("title", "tag", "slug"), "description")}),
        (_("COOKING"), {"fields": (("serves", "prep", "cook"), "method")}),
    )
    list_display = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ingredient_list_inline, cookbook_list_inline]


@admin.register(Foodstuff)
class FoodstuffAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "foodstuff", "form"]
    ordering = ["foodstuff__name"]
    inlines = [ingredient_list_inline]


@admin.register(IngredientList)
class IngredientListAdmin(admin.ModelAdmin):
    list_display = [
        "recipe",
        "ingredient",
        "qty",
        "uom",
    ]
    ordering = ["recipe"]
    list_filter = ["recipe", "ingredient"]
    search_fields = ["recipe", "ingredient"]


@admin.register(CookBookList)
class CookBookListAdmin(admin.ModelAdmin):
    list_display = ["cookbook", "recipe", "page", "url"]
    search_fields = ["cookbook", "recipe"]
