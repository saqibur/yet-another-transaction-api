# Standard library imports

# Django imports
from django.urls import path
from rest_framework.routers import SimpleRouter

# Third party imports


# Local imports
from apps.transaction.api.v1.views import TransactionModelViewSet

app_name = "transaction"


router = SimpleRouter()
router.register("", TransactionModelViewSet)

urlpatterns = [] + router.urls
