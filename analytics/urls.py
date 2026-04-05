from django.urls import path
from .views import *

urlpatterns = [
    path("analytics/summary/", monthly_summary),
    path("analytics/category/", category_breakdown),
    path("analytics/trends/", monthly_trends)
]