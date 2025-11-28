from django.urls import path, include, re_path
from blog import views



urlpatterns = [
    re_path(r"^index/(?P<id>\d{1})/$", views.index),
    path('', views.index),
    path('access/<int:age>/', views.access),
]

