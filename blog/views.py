from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect, HttpResponseNotFound, HttpResponseBadRequest, HttpResponseForbidden

def index(request, id):
    id = int(id)
    people = [None, 'Bob', 'Sam', 'Tom']
    # если пользователь найден возвращаем его
    if id in range(1, len(people)):
        return HttpResponse(people[id])
    # если не найден то 404
    else:
        return HttpResponseNotFound('Not found')

def access(requestm, age):
    # если возраст не в диапозоне 1 до 100
    if age not in range(1, 101):
        return HttpResponseBadRequest('Некорректные данные')
    if age < 18:
        return HttpResponseForbidden('Доступ заблокирован')
    else:
        return HttpResponse('Доступ разрешен')