from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("budgets", BudgetViewSet, basename="budget")

urlpatterns = router.urls

