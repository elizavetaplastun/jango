# Generated by Django 4.0.5 on 2022-07-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0018_reviews_view_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='post_url',
            field=models.CharField(default='', max_length=160),
        ),
    ]