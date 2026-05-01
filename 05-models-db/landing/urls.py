
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('city/<str:city>/', views.city_detail, name="city")
]
