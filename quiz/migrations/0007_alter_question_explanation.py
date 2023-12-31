# Generated by Django 4.0.8 on 2023-06-07 21:34

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_alter_question_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='explanation',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, help_text='Объяснение, которое будет показано после ответа на вопрос.', max_length=2000, verbose_name='Объяснение'),
        ),
    ]
