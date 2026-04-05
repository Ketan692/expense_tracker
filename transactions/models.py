from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Category(models.Model):
    CATEGORY_TYPE = (
        ("INCOME", "Income"),
        ("EXPENSE", "Expense")
    )

    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=CATEGORY_TYPE)

    def __str__(self):
        return f"{self.name} ({self.type})"
    

class Transaction(models.Model):
    TRANSACTION_TYPE = (
        ("INCOME", "Income"),
        ("EXPENSE", "Expense")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transactions")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TRANSACTION_TYPE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="transactions")
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def clean(self):
        if self.category.type != self.type:
            raise ValidationError("Category type must match transaction type.")

    def __str__(self):
        return f"{self.user.username} - {self.amount} ({self.type})"
    
    