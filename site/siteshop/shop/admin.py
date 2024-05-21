from django.contrib import admin
from .models import *

from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class NewsForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class InfoForm(forms.ModelForm):
    info = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class ItemShopAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = InfoForm
    save_as = True
    save_on_top = True
    list_display = ('id_item', 'title', 'cost')
    list_display_links = ('id_item', 'title')
    search_fields = ('title', )
    list_filter = ('cost', )


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = NewsForm
    save_as = True
    save_on_top = True
    list_display = ('date', 'title')
    list_display_links = ('date', 'title')
    search_fields = ('title', )
    list_filter = ('date',)
    ordering = ('-date', '-title')


class UsersAdmin(admin.ModelAdmin):
    save_as = True
    save_on_top = True
    list_display = ('id_user', 'name')
    list_display_links = ('id_user', 'name')
    search_fields = ('name', )
    list_filter = ('name', )


admin.site.register(ItemShop, ItemShopAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Carts)
admin.site.register(News, NewsAdmin)
