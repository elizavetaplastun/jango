# Generated by Django 4.0.5 on 2022-07-27 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0019_reviews_post_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email_phone', models.EmailField(max_length=254, verbose_name='Email или телефон')),
            ],
        ),
    ]
