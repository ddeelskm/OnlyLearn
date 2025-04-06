from django import forms

from courses.models import Category, Authors, Courses


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Название категории:',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class AuthorsForm(forms.ModelForm):
    class Meta:
        model = Authors
        fields = ['name', 'surname', 'description', 'photo']
        labels = {
            'name': 'Имя:',
            'surname': 'Фамилие:',
            'description': 'Описание:',
            'photo': 'Фото',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
        }


class CoursesForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title', 'author', 'images', 'cat', 'program', 'about', 'initial_requirements', 'courses_for', 'lessons', 'tests', 'tasks']
        labels = {
            'title': 'Название курса:',
            'author': 'Автор курса:',
            'images': 'Аватарка курса:',
            'cat': 'Категория:',
            'program': 'Программа курса:',
            'about': 'О курсе:',
            'initial_requirements': 'Начальные требования:',
            'courses_for': 'Для кого:',
            'lessons': 'Количество уроков:',
            'tests': 'Количество тестов:',
            'tasks': 'Интерактивных задач',
        }
