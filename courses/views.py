from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, TemplateView

from core.utils import DataMixins
from courses.forms import CoursesForm, AuthorsForm, CategoryForm
from courses.models import Courses, Authors, Category


# Create your views here.
class AddCourses(DataMixins, CreateView):
    model = Courses
    form_class = CoursesForm
    template_name = 'courses/addcourses.html'
    success_url = reverse_lazy('courses')
    title_page = 'Добавление курса'


class AddAuthors(DataMixins, CreateView):
    models = Authors
    form_class = AuthorsForm
    template_name = 'courses/addauthors.html'
    success_url = reverse_lazy('courses')
    title_page = 'Добавление автора'


class AddCategory(DataMixins, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'courses/addcategory.html'
    success_url = reverse_lazy('courses')
    title_page = 'Добавление категории'


class CoursesView(DataMixins, TemplateView):
    template_name = 'courses/courses.html'
    title_page = 'Курсы'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['authors'] = Authors.objects.all()
        context['courses'] = Courses.objects.all()
        context['category'] = Category.objects.all()
        return context
