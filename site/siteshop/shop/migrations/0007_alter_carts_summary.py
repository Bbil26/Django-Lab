# Generated by Django 5.0.4 on 2024-04-29 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_carts_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carts',
            name='summary',
            field=models.FloatField(blank=True, max_length=20),
        ),
    ]