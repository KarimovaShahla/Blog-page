# Generated by Django 5.0.6 on 2024-09-17 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_postimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='image_1',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/advertisements/images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='advertisements',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/advertisements/images/%Y/%m/%d/'),
        ),
        migrations.AddField(
            model_name='advertisements',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/advertisements/images/%Y/%m/%d/'),
        ),
    ]