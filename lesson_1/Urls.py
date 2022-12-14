from django.urls import path
from lesson_1 import views

urlpatterns = [
    path('', views.main, name="main"),
    path("rezumeform/", views.rez_post, name="createrezum"),
    path('feedback/', views.CreateFeedback.as_view(), name="createfeedback"),
    path('Gallery/<slug:slug>/', views.Post_detail_view.as_view(), name="Post"),
    path('Gallery/', views.Post_view.as_view(), name="Gallery"),
    path('Licences/', views.Licences_page, name="Licences"),
    path("Imploding_work/", views.Imploding_work, name="Imploding_work"),
    path("Demining/", views.Demining, name="Demining"),
    path("About_us/", views.About_us_page, name="About_us"),
    path("Vacancies/", views.Vacancies, name="Vacancies"),
    path("Clients/", views.Clients_v, name="Clients"),
    path("Equipment/", views.Equipment_page, name="Equipment"),

]
