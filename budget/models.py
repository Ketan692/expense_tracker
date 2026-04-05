from django.db import models
from django.contrib.auth.models import User
from transactions.models import *

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budgets")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    limit = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.DateField()

    class Meta:
        unique_together = ("user", "category", "month")

    def __str__(self):
        return f"{self.user.username} - {self.category.name} - {self.limit}"

