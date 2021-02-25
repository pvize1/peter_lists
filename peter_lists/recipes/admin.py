from django.contrib import admin
from .models import Foodstuff, Ingredient, IngredientList, Recipe


class role_inline(admin.TabularInline):
    model = IngredientList
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
    ]
    prepopulated_fields = {"slug": ("title",)}
    inlines = [role_inline]


@admin.register(Foodstuff)
class FoodstuffAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ["foodstuff", "form"]
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
