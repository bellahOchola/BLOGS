# Generated by Django 4.0.4 on 2022-06-06 12:29

from django.db import migrations
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    dependencies = [
        ('newsite', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_pic',
            field=pyuploadcare.dj.models.ImageField(blank=True),
        ),
    ]