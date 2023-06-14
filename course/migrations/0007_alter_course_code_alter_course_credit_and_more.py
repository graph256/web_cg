# Generated by Django 4.0.8 on 2023-06-05 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_courseoffer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=200, null=True, unique=True, verbose_name='Код'),
        ),
        migrations.AlterField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=0, null=True, verbose_name='Часы'),
        ),
        migrations.AlterField(
            model_name='course',
            name='is_elective',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Выборочный курс'),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('Бакалавр', 'Степень бакалавр'), ('Магистр', 'Степень магистра')], max_length=25, null=True, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='course',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.program', verbose_name='Программа'),
        ),
        migrations.AlterField(
            model_name='course',
            name='semester',
            field=models.CharField(choices=[('Первый', 'Первый'), ('Второй', 'Второй')], max_length=200, verbose_name='Семестр'),
        ),
        migrations.AlterField(
            model_name='course',
            name='summary',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='course',
            name='year',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (4, '5'), (4, '6')], default=0, verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='program',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='program',
            name='title',
            field=models.CharField(max_length=150, unique=True, verbose_name='Название'),
        ),
    ]
