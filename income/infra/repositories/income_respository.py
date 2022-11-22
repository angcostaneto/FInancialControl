from decimal import *
from http.client import BAD_REQUEST

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from domain.entities.income_entity import IncomeEntity
from domain.dtos.create_income_dto import CreateIncomeDto


class IncomeRepository:
    def get_by_id(self, reference):
        try:
            return IncomeEntity.objects.get(id=reference)
        except ObjectDoesNotExist:
            return None

    def create_income(self, income: CreateIncomeDto):
        try:
            return IncomeEntity.objects.create(
                value = Decimal(income.value), 
                user = income.user)
        except BAD_REQUEST:
            return None

    def delete_income(self, reference):
        try:
            return IncomeEntity.objects.delete(id=reference)
        except ObjectDoesNotExist:
            return None