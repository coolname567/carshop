from django.urls import path
import django.contrib.auth.views as auth_views
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(),name='login'),
]