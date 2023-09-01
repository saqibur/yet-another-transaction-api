from django.urls import (
    include,
    path,
)

from common.constants import API_V1

app_name = "transaction"

urlpatterns = [
    path(
        f"{API_V1}/transactions/",
        include(("apps.transaction.api.v1.urls", API_V1), namespace=API_V1),
    ),
]
