# Generated by Django 3.2.4 on 2021-06-23 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True, verbose_name='Дата добавления изображения')),
                ('image', models.ImageField(blank=True, upload_to='origin_img/%Y-%m-%d', verbose_name='Файл')),
                ('url', models.URLField(blank=True, max_length=255, verbose_name='Ссылка')),
                ('width', models.IntegerField(blank=True, null=True, verbose_name='Ширина')),
                ('height', models.IntegerField(blank=True, null=True, verbose_name='Высота')),
                ('custom_image', models.ImageField(blank=True, upload_to='custom_img/%Y-%m-%d')),
            ],
        ),
    ]