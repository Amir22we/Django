from django.urls import path, include, re_path
from django.views.generic import TemplateView
from blog import views



urlpatterns = [
    path('', views.index),
    path('about/', TemplateView.as_view(template_name='blog/about.html', extra_context={'header': 'О сайте'}))
]

