from django.db import models
from slugify import slugify


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=100, blank=False, unique=True, verbose_name='Ссылка')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, max_length=100)
        super().save(*args, **kwargs)


class Authors(models.Model):
    name = models.CharField(max_length=30, blank=False, verbose_name='Имя')
    surname = models.CharField(max_length=100, blank=False, verbose_name='Фамилие')
    photo = models.ImageField(upload_to='authors_corses/%Y/%m/', blank=False, verbose_name='Фото')
    description = models.TextField(max_length=255, blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=100, unique=True, blank=False, verbose_name='Ссылка')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name} {self.surname}', max_length=100)
        super().save(*args, **kwargs)


class Courses(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Название курса')
    images = models.ImageField(upload_to='avatar_courses/%Y/%m/', blank=False, verbose_name='Аватарка курсаа')
    program = models.TextField(blank=False, verbose_name='Программа курса')
    about = models.TextField(blank=False, verbose_name='О курсе')
    initial_requirements = models.TextField(blank=False, verbose_name='Начальные требования')
    courses_for = models.TextField(blank=False, verbose_name='Для кого')
    lessons = models.IntegerField(blank=False, default=0, verbose_name='Уроков')
    tests = models.IntegerField(blank=False, default=0, verbose_name='Тестов')
    tasks = models.IntegerField(blank=False, default=0, verbose_name='интерактивных задач')
    slug = models.SlugField(max_length=255, blank=False, unique=True, verbose_name='Ссылка')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    cat = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='catcourses', verbose_name='Категория')
    author = models.ForeignKey(Authors, on_delete=models.PROTECT, related_name='mycourses', verbose_name='Автор курса')

    class Meta:
        ordering = ['-time_create']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, max_length=255)
        super().save(*args, **kwargs)
