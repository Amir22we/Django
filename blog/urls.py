from django.urls import path
from blog import views

urlpatterns = [
    path('', views.index),
    path('about/<str:name>/<int:age>/', views.about), 
    path('about/<str:name>/', views.about),
    path('about/', views.about), 
    path('contact/', views.contact),

]
