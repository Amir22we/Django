from django.shortcuts import render 
from django.template.response import TemplateResponse

def index(request):
    return render(request, 'blog/index.html')