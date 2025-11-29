from django.shortcuts import render 
from django.template.response import TemplateResponse

def index(request):
    header = "Данные пользователя" # переменная
    langs = ['Python', 'Java', 'c#'] # список
    user = {'name': 'Tom', 'age': 22} # словарь
    address = ('Абрикосовая', 23, 45) # кортеж

    data = {'header': header, 'langs': langs, 'user': user, 'address': address}
    return render(request, 'blog/index.html', context=data)

def about(request):
    return TemplateResponse(request, 'blog/index.html')

