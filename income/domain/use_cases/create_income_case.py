from income.infra.repositories.income_respository import IncomeRepository
from income.domain.dtos.create_income_dto import CreateIncomeDto
from income.domain.dtos.get_income_dto import GetIncomeDTO
from income.domain.entities.income_entity_serializer import IncomeEntitySerializer
from rest_framework.response import Response
from rest_framework import status



class CreateIncomeCase:
  def __init__(self, repository: IncomeRepository) -> None:
    self._repository = repository

  def execute(self, income: CreateIncomeDto) -> GetIncomeDTO:
    serializer = IncomeEntitySerializer(income)
    if serializer.is_valid():
      self._repository.create_income(income)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
