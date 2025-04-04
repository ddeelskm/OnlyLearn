from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
menu = [
    {'title': 'Курсы', 'url_page': 'courses'},
    {'title': 'Игры', 'url_page': 'games'},
    {'title': 'Английский', 'url_page': 'english'},
    {'title': 'О сайте', 'url_page': 'about'},
    {'title': 'Контакты', 'url_page': 'contact'},
    {'title': 'Вход', 'url_page': 'login'},
    {'title': 'Регистрация', 'url_page': 'registration'},
        ]


def index(request):
    return render(request, 'core/index.html', context={'menu': menu})


def contacts(request):
    return HttpResponse('contact}')


def about(request):
    return HttpResponse('about')


def login(request):
    return HttpResponse('login')


def registration(request):
    return HttpResponse('registration')