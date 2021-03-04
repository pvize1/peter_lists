from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe


# Create your views here.
def RecipeHome(request):
    text = "Hello"
    recipe_list = Recipe.objects.filter(tag__icontains="chicken")
    count = recipe_list.count()
    return render(
        request,
        "recipes/recipes_home.html",
        {"text": text, "recipe_list": recipe_list, "count": count},
    )


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipes_detail.html"
