# Generated by Django 4.0.8 on 2023-06-12 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_alter_question_content_alter_question_explanation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='figure',
        ),
    ]