# Generated by Django 4.0.5 on 2022-07-12 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0010_license'),
    ]

    operations = [
        migrations.AddField(
            model_name='license',
            name='date_of_lic',
            field=models.DateField(default=datetime.date.today, null=True, verbose_name='Дата выдачи(если есть)'),
        ),
        migrations.AddField(
            model_name='license',
            name='number_of_lic',
            field=models.CharField(max_length=300, null=True, verbose_name='Номер документа(если есть)'),
        ),
        migrations.AddField(
            model_name='license',
            name='organ_poluch',
            field=models.CharField(max_length=150, null=True, verbose_name='Орган, выдавший документ'),
        ),
        migrations.AddField(
            model_name='license',
            name='other_txt',
            field=models.TextField(null=True, verbose_name='Дополнительная информация'),
        ),
        migrations.AddField(
            model_name='license',
            name='time_of_live',
            field=models.CharField(max_length=150, null=True, verbose_name='Срок действия'),
        ),
    ]