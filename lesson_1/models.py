from django.db import models
from datetime import date
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
from django.utils import timezone


class Work_type(models.Model):
    name = models.CharField("Тип работы", max_length=50)
    descriptiom = models.TextField("Описание типа работы", max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Тип работ"
        verbose_name_plural = "Типы работ"


class Poster(models.Model):
    name = models.CharField("Название статьи", max_length=100)
    description = RichTextField("Описание")
    poster_img = models.ImageField("Картинка", upload_to="posters_img/")
    date = models.DateField("Дата проделанной работы", default=date.today)
    place = models.CharField("Место", max_length=100, default="SPB")
    work_type = models.ForeignKey(Work_type, verbose_name="Типы", on_delete=models.SET_NULL, null=True)
    draft = models.BooleanField("Черновик", default=False)
    url = models.SlugField("Ссылка(будет в адресной строке)", max_length=160,
                           unique=True, default="1")

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

    def __str__(self):
        return self.name

    def get_pict(self):
        return self.poster_img

    def get_absolute_url(self):
        return reverse("Post", kwargs={"slug": self.url})


class Pictures_f_posts(models.Model):
    name = models.CharField("Название", max_length=50)
    parent = models.ForeignKey(
        Poster, verbose_name="Прикрепить к работе(статье)", on_delete=models.SET_NULL, null=True
    )
    pict = models.ImageField("Картинка", upload_to="posters_img/", null=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Картинка для поста"
        verbose_name_plural = "Картинки для постов"


class License(models.Model):
    name = models.CharField("Название", max_length=110)
    description = RichTextField("Информация о документе", null=True, )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Лицензия"
        verbose_name_plural = "Лицензии"


class PictForLicences(models.Model):
    pict = models.ImageField("Фотография или скан документа", upload_to="LicenceImg/", )
    parent = models.ForeignKey(License, verbose_name="Прикрепить к", null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Картинка у лицензии"
        verbose_name_plural = "Картинки к лицензиям"


class Main_Bg_pictures(models.Model):
    picture = models.ImageField("Картинка", upload_to="image_change/image_main_bg")
    to_main = models.BooleanField("Показать на сайте", default=False)

    def __str__(self):
        return f"Картинка - {self.picture}"

    class Meta:
        verbose_name = "Картинка для заднего фона на главной"
        verbose_name_plural = "Картинки для заднего фона на главной"


class FeedbackModel(models.Model):
    name = models.CharField("Имя", max_length=100)
    email_phone = models.CharField("Email или телефон", max_length=150)
    ready = models.BooleanField("Заявка закрыта", default=False)

    def __str__(self):
        return f"{self.name} - {self.email_phone}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"



class RezumFormModel(models.Model):
    name = models.CharField("Имя", max_length=100)
    email_phone = models.CharField("Email или телефон", max_length=150)
    text = models.TextField("О человеке", blank=True, null=True)
    file_rez = models.FileField('Резюме', upload_to='rezums/')

    ready = models.BooleanField("Заявка закрыта", default=False)

    def __str__(self):
        return f"{self.name} - {self.email_phone}"

    class Meta:
        verbose_name = "Резюме"
        verbose_name_plural = "Резюме"


class Vacancy(models.Model):
    name = models.CharField("Название вакансии", max_length=100)
    description = RichTextField("Описание")
    draft = models.BooleanField("Черновик", default=False)

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"

    def __str__(self):
        return self.name


class Works_description(models.Model):
    imloding_work = RichTextField("описание под заголовком")
    demining = RichTextField("ОЧИСТКА МЕСТНОСТИ ОТ ВОП")
    br_work = RichTextField("БУРОВЗРЫВНЫЕ РАБОТЫ")
    demolition = RichTextField("ВАЛКА/СНОС НАПРАВЛЕННЫМ ВЗРЫВОМ ЗДАНИЙ И СООРУЖЕНИЙ")
    explosive_destruction = RichTextField("БЕЗВЗРЫВНОЕ РАЗРУШЕНИЕ СКАЛЬНЫХ ПАРОД И ЖБК")
    design = RichTextField("ПРОЕКТИРОВАНИЕ БВР")
    else_works = RichTextField("ИНЫЕ ВИДЫ ВЗРЫВНЫХ РАБОТ")

    class Meta:
        verbose_name = "Описание услуг"

    def __str__(self):
        return "Описание услуг"


class Works_description_main(models.Model):
    imloding_work = RichTextField("описание под заголовком")
    demining = RichTextField("ОЧИСТКА МЕСТНОСТИ ОТ ВОП")
    br_work = RichTextField("БУРОВЗРЫВНЫЕ РАБОТЫ")
    demolition = RichTextField("ВАЛКА/СНОС НАПРАВЛЕННЫМ ВЗРЫВОМ ЗДАНИЙ И СООРУЖЕНИЙ")
    explosive_destruction = RichTextField("БЕЗВЗРЫВНОЕ РАЗРУШЕНИЕ СКАЛЬНЫХ ПАРОД И ЖБК")
    design = RichTextField("ПРОЕКТИРОВАНИЕ БВР")

    class Meta:
        verbose_name = "Краткое описание услуг для главной"

    def __str__(self):
        return "Краткое описание услуг для главной"


class About_us_main(models.Model):
    equipment = RichTextField("оборудование")
    experience = RichTextField("наш опыт")
    standards = RichTextField("соответсвие стандартам")
    customers = RichTextField("заказчики")
    vacancies = RichTextField("вакансии")

    class Meta:
        verbose_name = "Краткое описание (о компании) для главной"

    def __str__(self):
        return "Краткое описание (о компании) для главной"


class About_us(models.Model):
    us = RichTextField("о нас")
    experience = RichTextField("наш опыт")
    standards = RichTextField("соответсвие стандартам")

    class Meta:
        verbose_name = "о компании"

    def __str__(self):
        return "о компании"


class Equipment(models.Model):
    name = models.CharField("Название", max_length=110)
    description = RichTextField("Описание", null=True, )
    equipment_img = models.ImageField("Картинка", upload_to="Equipment_img/")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"

    def get_pict(self):
        return self.equipment_img

class Clients(models.Model):
    client_img = models.ImageField("Картинка", upload_to="Clients_img/")

    def __str__(self):
        return f"заказчики"

    class Meta:
        verbose_name = "заказчик"
        verbose_name_plural = "заказчики"

    def get_pict(self):
        return self.client_img

