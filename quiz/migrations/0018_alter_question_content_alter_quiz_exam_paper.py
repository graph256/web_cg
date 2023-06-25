# Generated by Django 4.0.8 on 2023-06-25 15:59

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0017_alter_completedtask_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(help_text='Введите текст вопроса, который вы хотите отобразить', verbose_name='Вопрос'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='exam_paper',
            field=models.BooleanField(default=False, help_text='Если да, результат каждой попытки пользователя будет сохранен. Необходимо для маркировки.', verbose_name='Экзаменационный лист'),
        ),
    ]
