from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse


# Create your models here.

class BannerText(models.Model):
    title = models.CharField(max_length=255, blank=False, unique=True, verbose_name='Текст банера')
    published = models.BooleanField(default=True, verbose_name='Опубликовать')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    class Meta:
        ordering = ['-time_created']


class CustomerReviews(models.Model):
    name = models.CharField(max_length=255, blank=False, default='Аноним', verbose_name='Автор')
    reviews = models.TextField(blank=False, verbose_name='Отзыв', validators=[MinLengthValidator(15, 'Минимум 15 символов')])
    image = models.ImageField(upload_to='photo_reviews/%Y/%m/%d/', blank=True, default='photo_reviews/default.png')
    published = models.BooleanField(default=True, verbose_name='Опубликовать')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время написания')

    class Meta:
        ordering = ['-time_created']

    def get_absolute_url(self):
        return reverse('reviews', kwargs={'slug_reviews': self.id})
