from django.db import models


# Create your models here.

class BannerText(models.Model):
    title = models.CharField(min_length=20, max_length=255, blank=False, verbose_name='Текст банера')
    published = models.BooleanField(default=True, verbose_name='Опубликовать')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
