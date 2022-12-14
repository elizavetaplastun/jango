from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView, CreateView
from .models import Poster, License, Works_description_main, Main_Bg_pictures, \
    Works_description, \
    FeedbackModel, Vacancy, About_us_main, About_us, Equipment,PictForLicences,Clients, RezumFormModel

from .form import FeedbackForm, RezumForm
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings


def main(request):
    # вызов штмл файла
    lasts_post = Poster.objects.filter(draft=False).order_by("-id")[:8]
    lice = License.objects.all()
    lice_img = PictForLicences.objects.all()
    works_description_main = Works_description_main.objects.all()
    about_us_main = About_us_main.objects.all()
    vacancies = Vacancy.objects.all()
    bg_pict = Main_Bg_pictures.objects.filter(to_main=True)
    bg_pict_out = []
    bg_pict_f_l = []
    for index, p in enumerate(bg_pict):
        if index == 0:
            bg_pict_f_l.append(p)
        if p.to_main:
            bg_pict_out.append(p)

    return render(request, 'lesson_1/main.html', {
        "last_posts": lasts_post,
        "license": lice,
        "vacancies": vacancies,
        "bg_pict": bg_pict,
        "bg_last": bg_pict_f_l,
        "works_description_main": works_description_main,
        "about_us_main": about_us_main,
        "lice_img": lice_img,

    })


def Licences_page(request):
    return render(request, 'lesson_1/Licences.html', {

    })


def Imploding_work(request):
    works_description = Works_description.objects.all()
    return render(request, "lesson_1//Imploding_work.html/", {
        "works_description": works_description
    })


def Demining(request):
    works_description = Works_description.objects.all()
    return render(request, "lesson_1//Demining.html/", {
        "works_description": works_description
    })


def About_us_page(request):
    about_us = About_us.objects.all()
    return render(request, "lesson_1//About_us.html/", {
        "about_us": about_us
    })


def Equipment_page(request):
    equipment = Equipment.objects.all()
    return render(request, "lesson_1//Equipment.html/", {
        "equipment": equipment
    })


def Vacancies(request):
    vacancies = Vacancy.objects.all()
    return render(request, 'lesson_1/Vacancies.html', {
        "vacancies": vacancies
    })

def Clients_v(request):
    clients = Clients.objects.all()
    return render(request, "lesson_1//Clients.html/", {
        "clients": clients
    })




class Post_view(ListView):
    model = Poster
    queryset = Poster.objects.all()
    template_name = "lesson_1/Gallery.html"
    context_object_name = "post_list"
    paginate_by = 20


class Post_detail_view(DetailView):
    model = Poster
    context_object_name = "Post_"
    slug_field = "url"
    template_name = "lesson_1/Work_post.html"


class CreateFeedback(CreateView):
    model = FeedbackModel
    context_object_name = "feedb"
    form_class = FeedbackForm

    success_url = "/"

    def form_valid(self, form):

        form.instance.ready = False
        tsname = form.instance.name
        tsemail = form.instance.email_phone
        try:
            send_mail(f'Сообщение от {tsname}',
                      f'Отправлена заявка от {tsname} - {tsemail}',
                      settings.DEFAULT_FROM_EMAIL, settings.RECIPIENTS_EMAIL)
        except BadHeaderError:
            pass
            # print("SEND_ERROR")

        # print(form.instance.ready)
        self.object = form.save()
        return super().form_valid(form)


# class CreateRezum(CreateView):
#     model = RezumFormModel
#     # context_object_name = "rezumf"
#     form_class = RezumForm
#     template_name = "lesson_1/Vacancies.html"
#     success_url = "/"
#
#     def form_valid(self, form):
#         # print(form)
#         form.instance.ready = False
#         print(form)
#         self.object = form.save()
#         return super().form_valid(form)
def rez_post(request):
    if request.method == 'POST':
        form = RezumForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(request.POST)
    return render(request, 'lesson_1/Vacancies.html', )
