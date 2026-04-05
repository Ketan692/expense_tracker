from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class BudgetViewSet(ModelViewSet):
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Budget.objects.filter(user=self.request.user).select_related("category")
    
    
    def validate(self, data):
        user = self.context["request"].user
        category = data.get("category")
        month = data.get("month")

        if Budget.objects.filter(user=user, category=category, month=month).exists():
            raise serializers.ValidationError("Budget already exists for this category and month.")

        return data