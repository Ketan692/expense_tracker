from rest_framework import serializers
from .models import *
from datetime import datetime
from django.db.models import Sum
from budget.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class TransactionSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["user"]

    
    def validate(self, data):
        category = data.get("category")
        transaction_type = data.get("type")

        if category.type != transaction_type:
            raise serializers.ValidationError(
                "Category type must match transaction type."
            )
        return data
    

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data['user'] = user


        transaction = super().create(validated_data)

        if transaction.type == "EXPENSE":
            month_start = transaction.date.replace(day=1)

            budget = Budget.objects.filter(
                user=user,
                category=transaction.category,
                month=month_start
            ).first()

            if budget:
                total_spend = (
                    user.transactions.filter(
                        category = transaction.category,
                        type = "EXPENSE",
                        date__year = transaction.date.year,
                        date__month = transaction.date.month
                    ).aggregate(total=Sum("amount"))["total"] or 0
                )

                if total_spend > budget.limit:
                    transaction._budget_exceeded = True
        return transaction
    

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if hasattr(instance, "_budget_exceeded"):
            data["warning"] = "⚠️ Budget exceeded for this category."

        return data
    