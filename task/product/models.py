"""
Модуль, содержащий определения модели Продукта.
Модель содержит поля для хранения основных данных, таких как название, модель, завод и т.д.
"""

from django.db import models

from task.entrepreneur.models import IndividualEntrepreneur
from task.factory.models import Factory
from task.network.models import NetworkNode
from task.retail.models import RetailNetwork


class Product(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    release_date = models.DateField()
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE, related_name='products')
    retail_network = models.ForeignKey(RetailNetwork, on_delete=models.CASCADE, related_name='products', null=True)
    individual_entrepreneur = models.ForeignKey(IndividualEntrepreneur, on_delete=models.CASCADE,
                                                related_name='products', null=True)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    network_node = models.ForeignKey(NetworkNode, on_delete=models.CASCADE, related_name='products')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f"{self.name} ({self.model})"

