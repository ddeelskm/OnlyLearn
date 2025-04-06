from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView

from core.utils import DataMixins
from courses.forms import CoursesForm
from courses.models import Courses


# Create your views here.
class AddCourses(DataMixins, CreateView):
    model = Courses
    form_class = CoursesForm
    template_name = 'courses/addcourses.html'
    success_url = reverse_lazy('home')
    title_page = 'Добавление курса'
