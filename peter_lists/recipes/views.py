from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Recipe


# Create your views here.
def RecipeHome(request):
    text = "Hello"
    count = Recipe.objects.filter(tag__icontains='mushroom').count()
    return render(request, "recipes/recipes_home.html", {"text": text, "count": count})


class RecipeListView(ListView):
    model = Recipe
    template_name = "recipes/recipes_list.html"


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipes_detail.html"
