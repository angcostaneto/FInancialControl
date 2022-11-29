from decimal import *
from http.client import BAD_REQUEST

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from income.domain.entities.income_entity import IncomeEntity
from income.domain.dtos.create_income_dto import CreateIncomeDto


class IncomeRepository:
    def get_by_id(self, reference):
        try:
            return IncomeEntity.objects.get(id=reference)
        except ObjectDoesNotExist:
            return None

    def create_income(self, income: CreateIncomeDto):
        return IncomeEntity.objects.create(
            value = Decimal(income.value), 
            user = income.user)

    def delete_income(self, reference):
        try:
            return IncomeEntity.objects.delete(id=reference)
        except ObjectDoesNotExist:
            return None
