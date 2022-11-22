from dataclasses import dataclass


@dataclass
class CreateIncomeDto:
    value: str
    user: str
