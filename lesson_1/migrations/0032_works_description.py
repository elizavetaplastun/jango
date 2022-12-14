# Generated by Django 4.0.6 on 2022-09-20 09:39

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0031_vacancy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Works_description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('demining', ckeditor.fields.RichTextField(verbose_name='ОЧИСТКА МЕСТНОСТИ ОТ ВОП')),
                ('br_work', ckeditor.fields.RichTextField(verbose_name='БУРОВЗРЫВНЫЕ РАБОТЫ')),
                ('demolition', ckeditor.fields.RichTextField(verbose_name='ВАЛКА/СНОС НАПРАВЛЕННЫМ ВЗРЫВОМ ЗДАНИЙ И СООРУЖЕНИЙ')),
                ('explosive_destruction', ckeditor.fields.RichTextField(verbose_name='БЕЗВЗРЫВНОЕ РАЗРУШЕНИЕ СКАЛЬНЫХ ПАРОД И ЖБК')),
                ('design', ckeditor.fields.RichTextField(verbose_name='ПРОЕКТИРОВАНИЕ БВР')),
                ('else_works', ckeditor.fields.RichTextField(verbose_name='ИНЫЕ ВИДЫ ВЗРЫВНЫХ РАБОТ')),
            ],
            options={
                'verbose_name': 'Описание услуги',
                'verbose_name_plural': 'Описание услуг',
            },
        ),
    ]
