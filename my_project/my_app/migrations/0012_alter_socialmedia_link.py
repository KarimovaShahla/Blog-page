# Generated by Django 5.0.6 on 2024-09-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_rename_image_1_socialmedia_image1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='link',
            field=models.TextField(blank=True, max_length=256, null=True),
        ),
    ]