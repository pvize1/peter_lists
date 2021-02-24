from django.shortcuts import render
from django.views.generic import ListView
from .models import OrigamiModel

# Create your views here.
def OrigamiHome(request):
    return render(request, "origami/origami_home.html")

class OrigamiListView(ListView):
    model = OrigamiModel
    template_name = "origami/origami_list.html"
