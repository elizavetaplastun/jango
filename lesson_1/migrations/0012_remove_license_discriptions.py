# Generated by Django 4.0.5 on 2022-07-12 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0011_license_date_of_lic_license_number_of_lic_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='license',
            name='discriptions',
        ),
    ]