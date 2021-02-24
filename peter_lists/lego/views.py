from django.shortcuts import render
from django.views.generic import ListView
from.models import LegoSet

# Create your views here.
def LegoHome(request):
    return render(request, "lego/lego_home.html")

class LegoListView(ListView):
    model = LegoSet
    template_name = "lego/lego_list.html"

