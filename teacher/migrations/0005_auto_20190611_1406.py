# Generated by Django 2.2.1 on 2019-06-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0004_auto_20190607_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='headshot',
        ),
        migrations.AddField(
            model_name='teacher',
            name='profile_picture',
            field=models.FileField(blank=True, upload_to='teacher_image'),
        ),
    ]
