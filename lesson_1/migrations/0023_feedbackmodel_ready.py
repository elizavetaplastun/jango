# Generated by Django 4.0.5 on 2022-07-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0022_alter_feedbackmodel_email_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackmodel',
            name='ready',
            field=models.BooleanField(default=False, verbose_name='Заявка закрыта'),
        ),
    ]
