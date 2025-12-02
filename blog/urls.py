from django.urls import path, include, re_path
from blog import views



urlpatterns = [
    path('', views.index),
    path('about/', views.about),
]

