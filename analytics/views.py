from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db.models import F, Sum
from django.db.models.functions import TruncMonth
from transactions.models import *


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def monthly_summary(request):
    user = request.user

    year = request.query_params.get("year")
    month = request.query_params.get("month")

    transactions = Transaction.objects.filter(user=user)

    if year and month:
        transactions = transactions.filter(date__year=year, date__month=month)

    income = transactions.filter(type="INCOME").aggregate(total=Sum("amount"))["total"] or 0
    expense = transactions.filter(type="EXPENSE").aggregate(total=Sum("amount"))["total"] or 0

    return Response({
        "income": income,
        "expense": expense,
        "savings": income - expense
    })


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def category_breakdown(request):
    user = request.user

    data = (
        Transaction.objects
        .filter(user=user, type="EXPENSE")
        .values(category_name=F("category__name"))
        .annotate(total=Sum("amount"))
        .order_by("-total")
    )

    return Response(data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def monthly_trends(request):
    user = request.user

    data = (
        Transaction.objects
        .filter(user=user, type="EXPENSE")
        .annotate(month=TruncMonth("date"))
        .values("month")
        .annotate(total=Sum("amount"))
        .order_by("month")
    )

    return Response(data)
