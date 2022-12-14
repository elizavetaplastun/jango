# Generated by Django 4.0.5 on 2022-08-20 16:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0027_remove_poster_budgat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='date_of_lic',
        ),
        migrations.RemoveField(
            model_name='license',
            name='number_of_lic',
        ),
        migrations.RemoveField(
            model_name='license',
            name='organ_poluch',
        ),
        migrations.RemoveField(
            model_name='license',
            name='other_txt',
        ),
        migrations.RemoveField(
            model_name='license',
            name='time_of_live',
        ),
        migrations.AddField(
            model_name='license',
            name='description',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='Информация о документе'),
        ),
    ]