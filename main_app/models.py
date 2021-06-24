from django.db import models
from django.urls import reverse


class Image(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя файла', blank=True)
    timestamp = models.DateField(auto_now_add=True, verbose_name='Дата добавления изображения')
    image = models.ImageField(verbose_name='Файл', upload_to='origin_img/%Y-%m-%d-%s', blank=True)
    url = models.URLField(max_length=255, blank=True, verbose_name='Ссылка')
    width = models.IntegerField(verbose_name='Ширина', blank=True, null=True)
    height = models.IntegerField(verbose_name='Высота', blank=True, null=True)
    custom_image = models.ImageField(upload_to='custom_img/%Y-%m-%d-%s', blank=True)

    def __str__(self):
        return str(self.id)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.id})


