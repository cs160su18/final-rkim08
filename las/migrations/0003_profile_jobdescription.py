# Generated by Django 2.0 on 2018-08-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('las', '0002_auto_20180808_0924'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='jobDescription',
            field=models.TextField(blank=True),
        ),
    ]
