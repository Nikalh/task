from rest_framework import serializers

from task.entrepreneur.models import IndividualEntrepreneur


class IndividualEntrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndividualEntrepreneur
        fields = '__all__'