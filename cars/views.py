from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cars.models import Car
class CarListView(ListView):
    model = Car
    template_name = 'cars/home.html'
    context_object_name = 'car_list'
# Create your views here.
class CarDetailView(DetailView):
    model = Car
    context_object_name = "car"
def home(request):
    return render (request,'home.html')