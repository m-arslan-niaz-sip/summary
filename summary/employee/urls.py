from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('employees', get_employees),
    path('employee/<int:employee_id>', get_employee),
    path('save', create_employee),
    path('salary/<int:employee_id>', get_salary),
]