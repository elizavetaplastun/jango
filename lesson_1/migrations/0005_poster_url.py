# Generated by Django 4.0.5 on 2022-06-28 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0004_pictures_f_posts_descriptiom'),
    ]

    operations = [
        migrations.AddField(
            model_name='poster',
            name='url',
            field=models.SlugField(default='1', max_length=160, unique=True, verbose_name='Ссылка(будет в адресной строке)'),
        ),
    ]