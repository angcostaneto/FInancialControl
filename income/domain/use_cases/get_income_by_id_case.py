from infra.repositories.income_respository import IncomeRepository
from dtos.get_income_dto import GetIncomeDTO

class GetIncomeByIdCase:
  def __init__(self, repository: IncomeRepository) -> None:
    self.__repository = repository

  def execute(self, reference: str) -> GetIncomeDTO:
    return self.__repository.get_by_id(reference)