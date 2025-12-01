from django.shortcuts import render 
from django.template.response import TemplateResponse

def index(request):
    cat = ['Python', 'Java', 'JS', 'Go', 'C#', 'Kotlin']
    return render(request, 'blog/index.html', context={'cat': cat})
