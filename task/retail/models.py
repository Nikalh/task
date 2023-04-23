"""
Модуль, содержащий определения модели Розничной сети.
Модель содержит поля для хранения основных данных, таких как название, адрес, электронная почта и т.д.
"""

from django.db import models

from task.factory.models import Factory


class RetailNetwork(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='retail_networks', null=True)

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'

    def __str__(self):
        return self.name

