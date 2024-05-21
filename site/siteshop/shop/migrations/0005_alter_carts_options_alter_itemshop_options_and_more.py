# Generated by Django 5.0.4 on 2024-04-24 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_item_shop_itemshop'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carts',
            options={'ordering': ['id_user'], 'verbose_name': 'Корзина', 'verbose_name_plural': 'Корзины пользователей'},
        ),
        migrations.AlterModelOptions(
            name='itemshop',
            options={'ordering': ['id_item'], 'verbose_name': 'Товар магазина', 'verbose_name_plural': 'Товары магазина'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['date'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'ordering': ['id_user'], 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
