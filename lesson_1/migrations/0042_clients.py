# Generated by Django 4.0.6 on 2022-09-23 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0041_alter_rezumformmodel_file_rez_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_img', models.ImageField(upload_to='Clients_img/', verbose_name='Картинка')),
            ],
            options={
                'verbose_name': 'заказчик',
                'verbose_name_plural': 'заказчики',
            },
        ),
    ]