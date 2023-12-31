# Generated by Django 4.0.8 on 2023-06-07 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_newsandevents_posted_as_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsandevents',
            name='posted_as',
            field=models.CharField(choices=[('News', 'Новость'), ('Events', 'Событие')], max_length=10, verbose_name='Записать как:'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='semester',
            field=models.CharField(blank=True, choices=[('First', 'Первый'), ('Second', 'Второй')], max_length=10, verbose_name='Семестр'),
        ),
    ]
