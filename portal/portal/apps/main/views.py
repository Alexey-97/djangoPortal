from django.http import HttpResponse


def index(request):
    return HttpResponse("«Это главная страница нашего корпоративного портала.»")
