# Generated by Django 4.0.8 on 2023-06-18 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_user_hist_static'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='hist_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
