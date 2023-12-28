import uuid

from django.db import models


class TimeBaseModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Акция добавлена')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Акция обновлена')


class Stock(TimeBaseModel):
    class Meta:
        verbose_name = "Акция"
        verbose_name_plural = "Акции"

    id = models.UUIDField(primary_key=True)
    name_stock = models.CharField(max_length=100, verbose_name="Название акции")
    description_stock = models.CharField(max_length=250, verbose_name="Описание акции")
    price_stock = models.CharField(max_length=20, verbose_name="Размер скидки или кэшбека")
    category = models.CharField(max_length=3, verbose_name="Категория акции")
    start_date_stock = models.DateField(verbose_name="Дата старта акции")
    end_date_stock = models.DateField(verbose_name="Дата окончания акции")

    def __str__(self):
        return f"{self.name_stock} - категория {self.category}"
