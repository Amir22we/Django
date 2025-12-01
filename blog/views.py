from django.shortcuts import render 
from django.template.response import TemplateResponse

def index(request):
    return render(request, 'blog/index.html', context={'body': '<h1>Hello World</h1>'})
