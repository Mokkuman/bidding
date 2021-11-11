# Generated by Django 3.2.7 on 2021-11-11 07:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20211111_0100'),
        ('users', '0010_alter_user_profilepic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='products',
            new_name='cartStockProducts',
        ),
        migrations.AlterField(
            model_name='bid',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.bidproduct'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
