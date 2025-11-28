from django.urls import path, include 
from blog import views



urlpatterns = [
    path('', views.index),
    path('index/<int:id>/', views.index),
    path('access/<int:age>/', views.access),
    
]

