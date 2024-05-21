from django.db import models
from django.urls import reverse

'''
Item_Shop
=============
id_item, title, cost, info, ico, slug

Users
============
id_user, name, login, password

Cart
==========
id_user, id_item, count, cost, summary

News
==========
date, title, content, slug
'''


class ItemShop (models.Model):
    id_item = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=40, unique=True)
    cost = models.FloatField(max_length=12)
    info = models.CharField(max_length=250)
    ico = models.CharField(max_length=200)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id_item']
        verbose_name = 'Товар магазина'
        verbose_name_plural = 'Товары магазина'


class Users (models.Model):
    id_user = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40)
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=40)

    def __str__(self):
        str_out = str(self.id_user) + " " + str(self.name)
        return str_out

    class Meta:
        ordering = ['id_user']
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Carts (models.Model):
    id_user = models.IntegerField()
    id_item = models.IntegerField()
    count = models.IntegerField()
    title = models.CharField(max_length=40, blank=True)
    summary = models.FloatField(max_length=20, blank=True)

    def __str__(self):
        return str(self.id_item)

    class Meta:
        ordering = ['id_user']
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины пользователей'

    def save(self, *args, **kwargs):

        item_shop = ItemShop.objects.get(id_item=self.id_item)
        self.title = item_shop.title
        self.summary = self.count * item_shop.cost

        super().save(*args, **kwargs)


class News (models.Model):
    date = models.DateField()
    title = models.CharField(max_length=40)
    content = models.CharField(max_length=600)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Новости'

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={"slug": self.slug})

