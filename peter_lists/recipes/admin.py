from django.contrib import admin
from .models import Foodstuff, Ingredient, IngredientList, Recipe, CookBookList


class role_inline(admin.TabularInline):
    model = IngredientList
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["title", "description"]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [role_inline]


@admin.register(Foodstuff)
class FoodstuffAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["name", "foodstuff", "form"]
    ordering = ["foodstuff__name"]
    inlines = [role_inline]


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
    list_display = ["cookbook", "recipe"]
