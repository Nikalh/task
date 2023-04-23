"""
Модуль, содержащий определения моделей базы данных.
Модели:
- Supplier: модель Поставщика.
- NetworkNode: модель Звена сети.
Все модели содержат поля для хранения основных данных, таких как название, адрес, электронная почта и т.д.
"""
from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name


class NetworkNode(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='network_nodes',
        null=True,
        blank=True,
    )
    level = models.PositiveIntegerField(default=0)


    class Meta:
        verbose_name = 'Звено сети'
        verbose_name_plural = 'Звенья сети'

    def __str__(self):
        return self.name
