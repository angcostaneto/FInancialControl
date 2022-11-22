from dataclasses import dataclass
from django.contrib.auth.models import User


@dataclass
class GetIncomeDTO:
    id: str
    value: str
    created_at: str
    updated_at: str
    user: User
