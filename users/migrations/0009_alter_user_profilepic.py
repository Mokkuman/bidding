# Generated by Django 3.2.7 on 2021-11-08 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profilePic',
            field=models.ImageField(blank=True, default='pic_default', null=True, upload_to=''),
        ),
    ]