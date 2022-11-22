from income.domain.dtos.create_income_dto import CreateIncomeDto
from infra.repositories.income_respository import IncomeRepository
from use_cases.create_income_case import CreateIncomeCase

def create_income_case_factory(income: CreateIncomeDto):
  income_repository = IncomeRepository()
  create_income_use_case = CreateIncomeCase(income_repository)
  return create_income_use_case.execute(income)