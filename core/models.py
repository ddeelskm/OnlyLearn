from django.core.validators import MinLengthValidator
from django.db import models


# Create your models here.

class BannerText(models.Model):
    title = models.CharField(max_length=255, blank=False, verbose_name='Текст банера')
    published = models.BooleanField(default=True, verbose_name='Опубликовать')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')


class CustomerReviews(models.Model):
    name = models.CharField(max_length=255, blank=False, default='Аноним', verbose_name='Автор')
    reviews = models.TextField(blank=False, min_length=MinLengthValidator(20), verbose_name='Отзыв')
    image = models.ImageField(upload_to='photo_reviews/', blank=True, null=True)
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время написания')



