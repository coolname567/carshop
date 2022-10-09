from django.urls import path
from cars.models import Car
from cars.views import home
from cars.views import CarListView,CarDetailView
urlpatterns = [
    path('', CarListView.as_view(), name="home"),
    path('<slug:slug>/',CarDetailView.as_view(),name='car_detail'),
    ]
