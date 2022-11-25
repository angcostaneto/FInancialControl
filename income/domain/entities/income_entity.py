import uuid

from django.contrib.auth.models import User
from django.db import models


class IncomeEntity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    value = models.DecimalField(max_digits=15, decimal_places=6)
    created_at = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
    updated_at = models.DateTimeField(auto_now=True, blank = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, blank = True, null = True)