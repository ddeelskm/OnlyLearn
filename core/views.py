from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, TemplateView, CreateView

from core.forms import BannerTextForm, CustomerReviewsForm
from core.models import CustomerReviews, BannerText
from core.utils import DataMixins
from courses.models import Courses, Authors


# Create your views here.


class AddReviews(DataMixins, CreateView):
    model = CustomerReviews
    form_class = CustomerReviewsForm
    template_name = 'core/addreviews.html'
    success_url = reverse_lazy('home')
    title_page = 'Добавить отзыв'


class AddBanner(DataMixins, CreateView):
    model = BannerText
    form_class = BannerTextForm
    template_name = 'core/addbaner.html'
    success_url = reverse_lazy('home')
    title_page = 'Добавление баннера'


class Index(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['banner'] = BannerText.objects.filter(published=1)[:5]
        context['reviews'] = CustomerReviews.objects.filter(published=1)[:4]
        context['courses'] = Courses.objects.all()[:4]
        context['authors'] = Authors.objects.all()[:4]
        return context


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена.</h1>')


def contacts(request):
    return HttpResponse('contact}')


def about(request):
    return HttpResponse('about')


def login(request):
    return HttpResponse('login')


def registration(request):
    return HttpResponse('registration')
