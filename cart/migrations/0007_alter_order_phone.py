# Generated by Django 4.1.dev20210924165208 on 2021-11-24 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_order_address_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]