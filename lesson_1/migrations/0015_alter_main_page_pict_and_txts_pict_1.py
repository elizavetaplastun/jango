# Generated by Django 4.0.5 on 2022-07-20 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson_1', '0014_links_name_main_bg_pictures_main_page_pict_and_txts_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main_page_pict_and_txts',
            name='pict_1',
            field=models.ImageField(default='image_change/Main_page_pict/cb_igm.png', upload_to='image_change/Main_page_pict', verbose_name='Картинка в блоке услуги'),
        ),
    ]