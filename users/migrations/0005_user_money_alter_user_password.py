# Generated by Django 4.1.dev20210924165208 on 2021-11-04 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_firstname'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.PositiveIntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
