# Generated by Django 4.0.8 on 2023-06-18 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0016_remove_completedtask_count_solutions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedtask',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
