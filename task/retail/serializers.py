from rest_framework import serializers

from task.retail.models import RetailNetwork


class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = '__all__'
