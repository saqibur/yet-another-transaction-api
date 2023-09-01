# Standard library imports

# Django imports
from rest_framework.viewsets import ModelViewSet


# Third party imports

# Local imports
from apps.transaction.api.v1.serializers import TransactionModelSerializer


class TransactionModelViewSet(ModelViewSet):
    http_method_names = [
        "get",
        "post",
    ]
    lookup_field = "uuid"
    authentication_classes = []
    permission_classes = []
    serializer_class = TransactionModelSerializer
    queryset = serializer_class.Meta.model.objects.all()
