from rest_framework import serializers
from income.domain.entities.income_entity import IncomeEntity

class IncomeEntitySerializer(serializers.ModelSerializer):
  class Meta:
    model = IncomeEntity
    fields = [
      'id',
      'value',
      'created_at',
      'updated_at',
      'user'
    ]