# Generated by Django 4.0.5 on 2022-06-25 08:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название статьи')),
                ('description', models.TextField(verbose_name='Описание')),
                ('poster_img', models.ImageField(upload_to='posters_img/', verbose_name='Картинка')),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Дата проделанной работы')),
                ('place', models.CharField(default='SPB', max_length=100, verbose_name='Место')),
                ('budgat', models.PositiveIntegerField(default=0, help_text='Указать стоимость(р)', verbose_name='Бюджет')),
                ('draft', models.BooleanField(default=False, verbose_name='Черновик')),
            ],
        ),
        migrations.CreateModel(
            name='Work_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Тип работы')),
                ('descriptiom', models.TextField(max_length=500, verbose_name='Описание типа работы')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='EMAIL')),
                ('text', models.TextField(max_length=1000, verbose_name='Отзыв')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='lesson_1.reviews', verbose_name='Родитель')),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lesson_1.poster', verbose_name='Статья')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
        migrations.AddField(
            model_name='poster',
            name='work_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lesson_1.work_type', verbose_name='Типы'),
        ),
    ]
