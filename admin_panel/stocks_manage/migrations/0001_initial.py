# Generated by Django 5.0 on 2023-12-27 12:45

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Акция добавлена')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Акция обновлена')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name_stock', models.CharField(max_length=100, verbose_name='Название акции')),
                ('description_stock', models.CharField(max_length=250, verbose_name='Описание акции')),
                ('price_stock', models.CharField(max_length=20, verbose_name='Размер скидки или кэшбека')),
                ('category', models.CharField(max_length=3, verbose_name='Категория акции')),
                ('start_date_stock', models.DateField(verbose_name='Дата старта акции')),
                ('end_date_stock', models.DateField(verbose_name='Дата окончания акции')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
    ]