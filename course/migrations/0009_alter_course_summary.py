# Generated by Django 4.0.8 on 2023-06-06 05:46

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_coursepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=0),
            preserve_default=False,
        ),
    ]
