from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe

# Create your views here.
def RecipeHome(request):
    return render(request, "recipes/recipes_home.html")


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipes_detail.html"
