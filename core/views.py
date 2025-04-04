from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
menu = ['Курсы', 'Игры', 'Английский', 'О сайте', 'Контакты', 'Вход', 'Регистрация']


def index(request):
    return HttpResponse('index')


def contacts(request):
    return HttpResponse('contact}')


def about(request):
    return HttpResponse('about')


def login(request):
    return HttpResponse('login')


def registration(request):
    return HttpResponse('registration')