# Standard library imports
from django.urls import (
    include,
    path,
)

# Django imports

# Third party imports
from decouple import config

# Local imports
from common.constants import LOCAL_SERVER

urlpatterns = [
    path("", include("apps.transaction.urls")),
]

if config("SERVER_NAME") in [LOCAL_SERVER]:
    from drf_spectacular.views import (
        SpectacularAPIView,
        SpectacularSwaggerView,
    )

    urlpatterns += [
        path("schema/", SpectacularAPIView.as_view(), name="schema"),
        path(
            "schema/swagger-ui/",
            SpectacularSwaggerView.as_view(url_name="schema"),
            name="swagger-ui",
        ),
    ]
