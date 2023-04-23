"""
Модуль, содержащий определения модели Завода.
Модель содержит поля для хранения основных данных, таких как название, адрес, электронная почта и т.д.
"""
from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'

    def __str__(self):
        return self.name
