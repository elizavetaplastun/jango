# Generated by Django 4.0.5 on 2022-07-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0012_remove_license_discriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pictures_f_posts',
            name='descriptiom',
            field=models.TextField(default=False, max_length=500, null=True, verbose_name='Описание типа работы'),
        ),
    ]
