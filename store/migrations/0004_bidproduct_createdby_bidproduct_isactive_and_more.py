# Generated by Django 4.1.dev20210924165208 on 2021-11-10 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_profilepic'),
        ('store', '0003_bidproduct_bidwinner'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidproduct',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bidCreator', to='users.user'),
        ),
        migrations.AddField(
            model_name='bidproduct',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='stockproduct',
            name='createdBy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productCreator', to='users.user'),
        ),
        migrations.AddField(
            model_name='stockproduct',
            name='isActive',
            field=models.BooleanField(default=True),
        ),
    ]
