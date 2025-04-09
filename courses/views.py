from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView

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
        cat_slug = self.request.GET.get('cat_slug')
        context['authors'] = Authors.objects.all()
        context['category'] = Category.objects.all()

        if cat_slug:
            context['courses'] = Courses.objects.filter(cat__slug=cat_slug)
        else:
            context['courses'] = Courses.objects.all()
        return context


class CoursesDetail(DataMixins, DetailView):
    model = Courses
    template_name = 'courses/coursesdetail.html'
    slug_url_kwarg = 'detail_slug'
    slug_field = 'slug'
    context_object_name = 'courses_detail'


class AuthorDetail(DataMixins, DetailView):
    model = Authors
    template_name = 'courses/author.html'
    slug_url_kwarg = 'author_slug'
    slug_field = 'slug'
    context_object_name = 'author_detail'
