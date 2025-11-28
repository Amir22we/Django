from django.http import HttpResponse 

def home_page_view(request):
    return HttpResponse('Hello, welcome to the Blog Home Page!')

def index(request):
    return HttpResponse('</h2>Welcome to the Blog Index Page</h2>')

def about(request, name = 'Undefined', age = 0):
    return HttpResponse(f'''
                    <h2>О пользователе</h2>
                    <p>Имя: {name}</p>
                    <p>Возраст: {age}</p>
                        ''')  

def contact(request):
    return HttpResponse('<h2>Contact the Blog</h2>') 

