# Generated by Django 5.0.6 on 2024-09-18 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_advertisements_image_1_advertisements_image_2_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postimage',
            options={'ordering': ['order'], 'verbose_name': 'Post Image', 'verbose_name_plural': 'Post Images'},
        ),
        migrations.RemoveField(
            model_name='advertisements',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='advertisements',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='advertisements',
            name='image_3',
        ),
    ]