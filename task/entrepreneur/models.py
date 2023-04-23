"""
Модуль, содержащий определения модели Индивидуального предпринимателя.
Модель содержит поля для хранения основных данных, таких как название, адрес, электронная почта и т.д.
"""
from django.db import models

from task.retail.models import RetailNetwork


class IndividualEntrepreneur(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=255)
    retail_network = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE, related_name='individual_entrepreneurs',
                                       null=True)

    class Meta:
        verbose_name = 'Индивидуальный предприниматель'
        verbose_name_plural = 'Индивидуальные предприниматели'

    def __str__(self):
        return self.name

