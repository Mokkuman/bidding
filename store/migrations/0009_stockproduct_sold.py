# Generated by Django 4.1.dev20210924165208 on 2021-11-24 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_bidproduct_condition'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockproduct',
            name='sold',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]