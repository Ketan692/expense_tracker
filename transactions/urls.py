from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("categories", CategoryViewSet)
router.register("transactions", TransactionViewSet)

urlpatterns = router.urls