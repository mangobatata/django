from django.urls import path
from . import views

urlpatterns = [
    # path('hello-world', views.index, name='index'),
    # path('hello/<str:name>/', views.greet, name='greet'),
    path("", views.index, name="index"),  # /messages
    path("<int:day>", views.days_week_with_number),
    path("<str:day>", views.days_week, name="day-quote")  # /messages/friday
]
