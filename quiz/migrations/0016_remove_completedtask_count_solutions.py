# Generated by Django 4.0.8 on 2023-06-18 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0015_remove_completedtask_is_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='completedtask',
            name='count_solutions',
        ),
    ]
