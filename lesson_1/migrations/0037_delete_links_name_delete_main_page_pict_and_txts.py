# Generated by Django 4.0.6 on 2022-09-21 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0036_works_description_main'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Links_name',
        ),
        migrations.DeleteModel(
            name='Main_page_pict_and_txts',
        ),
    ]
