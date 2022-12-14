from django.contrib import admin
# from django.contrib.gis import forms
# Register your models here.
from django.utils.safestring import mark_safe
# from ckeditor.widgets import CKEditorWidget
from .models import Poster, \
    Work_type, \
    Pictures_f_posts, \
    License, \
    Main_Bg_pictures, \
    FeedbackModel, \
    PictForLicences, \
    Vacancy, \
    Works_description, \
    Works_description_main, About_us_main, \
    About_us, Equipment, RezumFormModel, Clients


# @admin.register(PictForLicences)
# class PictForLicencesAdmin(admin.ModelAdmin):
#     list_display = ("id", "get_image", "parent")
#     list_display_links = ("id", "get_image",)
#     ordering = ("parent",)
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.pict.url} width="160" height="100">')
#
#     get_image.short_description = "Изображение"


@admin.register(Work_type)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name',)
    ordering = ('-id',)


class PictLicenceInline(admin.TabularInline):
    model = PictForLicences
    extra = 1
    readonly_fields = ("get_image",)
    fieldsets = (
        (None, {
            "fields": (('get_image', "pict",),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.pict.url} width="160" height="100">')

    get_image.short_description = "Изображение"


class PictPostInline(admin.TabularInline):
    model = Pictures_f_posts
    extra = 1
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            "fields": (('name',),)
        }),
        (None, {
            "fields": (('get_image', 'pict',),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.pict.url} width="160" height="100">')

    get_image.short_description = "Изображение"


@admin.register(Poster)
class PosterAdmin(admin.ModelAdmin):
    search_fields = ('name', 'work_type',)
    save_on_top = True
    list_display = ('id', 'name', 'get_image', 'work_type', 'draft',)
    list_display_links = ('id', 'name', 'get_image')
    list_editable = ('draft',)
    ordering = ('-id',)
    readonly_fields = ('get_image',)
    # form = PosterAdminForm
    list_filter = ('work_type', 'draft')
    fieldsets = (
        (None, {
            "fields": (('name',),)
        }),
        (None, {
            "fields": (('description',),)
        }),
        (None, {
            "fields": (('get_image', 'poster_img',),)
        }),
        (None, {
            "fields": (('date', 'place',),)
        }),
        (None, {
            "fields": (('work_type',),)
        }),
        (None, {
            "fields": (('url',),)
        }),
        (None, {
            "fields": (('draft',),)
        }),
    )
    inlines = [PictPostInline]

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster_img.url} width="160" height="100">')

    get_image.short_description = "Изображение"


@admin.register(License)
class LicenseAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    ordering = ('-id',)
    inlines = [PictLicenceInline]


# @admin.register(Pictures_f_posts)
# class Pictures_f_postsAdmin(admin.ModelAdmin):
#     list_filter = ('parent',)
#     list_display = ('name', 'get_image', 'parent',)
#     list_display_links = ('name', 'get_image',)
#     readonly_fields = ('get_image',)
#     ordering = ('parent',)
#     fieldsets = (
#         (None, {
#             "fields": (('name', 'parent'),)
#         }),
#         (None, {
#             "fields": (('get_image', 'pict',),)
#         }),
#     )
#
#     def get_image(self, obj):
#         return mark_safe(f'<img src={obj.pict.url} width="160" height="100">')
#
#     get_image.short_description = "Изображение"


@admin.register(Main_Bg_pictures)
class Main_Bg_picturesAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_image', 'to_main',)
    list_display_links = ('id', 'get_image',)
    list_editable = ('to_main',)
    readonly_fields = ('get_image_big',)
    ordering = ('-to_main',)
    fieldsets = (
        (None, {
            "fields": (('get_image_big',),)
        }),
        (None, {
            "fields": (('picture',),)
        }),
        (None, {
            "fields": (('to_main',),)
        }),
    )
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="160" height="100">')

    def get_image_big(self, obj):
        return mark_safe(f'<img src={obj.picture.url} width="1200" height="700">')

    get_image.short_description = "Изображение"
    get_image_big.short_description = "Изображение"


@admin.register(FeedbackModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email_phone', 'ready')
    list_display_links = ('name',)
    search_fields = ('name', 'email_phone',)
    list_filter = ('ready',)
    ordering = ('ready', '-id')
    readonly_fields = ('name', 'email_phone',)
    fieldsets = (
        (None, {
            "fields": (('name', 'email_phone'),)
        }),
        (None, {
            "fields": (('ready',),)
        }),
    )


@admin.register(RezumFormModel)
class FeedbackModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email_phone', 'ready')
    list_filter = ('ready',)
    ordering = ('ready', '-id')
    list_display_links = ('name',)
    search_fields = ('name', 'email_phone',)
    readonly_fields = ('name', 'email_phone',)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    save_on_top = True
    list_display = ('id', 'name', 'draft',)
    list_display_links = ('id', 'name',)
    list_editable = ('draft',)
    ordering = ('-id',)
    fieldsets = (
        (None, {
            "fields": (('name',),)
        }),
        (None, {
            "fields": (('description',),)
        }),
        (None, {
            "fields": (('draft',),)
        }),
    )


@admin.register(Works_description)
class Works_descriptionAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Works_description.objects.all().count() == 0:
            return True
        else:
            return False

        # Запрет на удаление объекта

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Works_description_main)
class Works_description_mainAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if Works_description_main.objects.all().count() == 0:
            return True
        else:
            return False

        # Запрет на удаление объекта

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(About_us_main)
class About_us_mainAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if About_us_main.objects.all().count() == 0:
            return True
        else:
            return False

        # Запрет на удаление объекта

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(About_us)
class About_usAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        if About_us.objects.all().count() == 0:
            return True
        else:
            return False

        # Запрет на удаление объекта

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    save_on_top = True
    list_display = ('id', 'name', 'get_image',)
    list_display_links = ('id', 'name', 'get_image')
    ordering = ('-id',)
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            "fields": (('name',),)
        }),
        (None, {
            "fields": (('description',),)
        }),
        (None, {
            "fields": (('get_image', 'equipment_img',),)
        }),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.equipment_img.url} width="160" height="100">')

    get_image.short_description = "Изображение"




@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('id', 'get_image',)
    list_display_links = ('id', 'get_image')
    ordering = ('-id',)
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            "fields": (('get_image', 'client_img',),)
        }),

    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.client_img.url} width="160" height="100">')

    get_image.short_description = "Изображение"



