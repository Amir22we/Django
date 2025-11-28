from django.http import HttpResponse 

def home_page_view(request):
    return HttpResponse('Hello, welcome to the Blog Home Page!')
