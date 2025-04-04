from django.urls import path

from core import views

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contacts, name='contact'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
]
