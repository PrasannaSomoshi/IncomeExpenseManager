from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Income(models.Model):
    income = models.IntegerField()
    incometype = models.CharField(max_length=25)
    incomeDate = models.DateField()
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Expense(models.Model):
    expense = models.IntegerField()
    expensetype = models.CharField(max_length=25)
    expenseDate = models.DateField()
    description = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
