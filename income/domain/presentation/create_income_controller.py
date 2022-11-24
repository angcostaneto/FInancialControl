from rest_framework import status
from rest_framework.decorators import api_view
from django.http import request
from income.domain.dtos.create_income_dto import CreateIncomeDto
from income.domain.use_cases.factory.create_income_case_factory import create_income_case_factory

@api_view(['GET'])
def create_income_controller(http_request: request):
  incomeData = CreateIncomeDto(
    value = http_request.data.get('value'),
    user = http_request.user.id
  )
  
  return create_income_case_factory(incomeData)
