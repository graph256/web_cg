# Generated by Django 4.0.8 on 2023-06-07 22:58

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_newsandevents_posted_as_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandevents',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
    ]