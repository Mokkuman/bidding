# Generated by Django 4.1.dev20210924165208 on 2021-11-20 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211111_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bidproduct',
            name='currentBid',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='bidproduct',
            name='minBid',
            field=models.FloatField(default=0),
        ),
    ]
