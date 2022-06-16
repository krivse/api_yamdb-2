# Generated by Django 2.2.16 on 2022-06-16 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='titles',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='titles',
            name='genre',
            field=models.ManyToManyField(through='reviews.GenreTitle', to='reviews.Genre', verbose_name='Жанр'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='year',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(2022)], verbose_name='Дата выхода'),
        ),
    ]
