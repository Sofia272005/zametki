# Generated by Django 4.2.8 on 2023-12-18 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='Тема заметки')),
                ('text', models.TextField(verbose_name='Текст заметки')),
                ('date', models.DateTimeField(verbose_name='Дата добавления')),
            ],
        ),
    ]