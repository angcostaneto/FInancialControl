from django.urls import path
from domain.presentation.create_income_controller import create_income_controller

urlpatterns = [
  path('create-income', create_income_controller)
]
