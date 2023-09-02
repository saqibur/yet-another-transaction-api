# Standard library imports

# Django imports
from django.db.models import Sum
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


# Third party imports

# Local imports
from apps.transaction.api.v1.serializers import (
    TransactionModelSerializer,
    ReportDateRangeSerializer,
)
from apps.transaction.services import TransactionService
from common.serializers import get_validated_query_parameters
from common.constants import SAR_TO_USD_RATE


class TransactionModelViewSet(ModelViewSet):
    http_method_names = [
        "get",
        "post",
    ]
    lookup_field = "uuid"
    serializer_class = TransactionModelSerializer
    queryset = serializer_class.Meta.model.objects.all()


class TransactionReport(APIView):
    def get(self, request, *args, **kwargs):
        validated_query_params = get_validated_query_parameters(
            ReportDateRangeSerializer,
            request,
        )

        from_date = validated_query_params.get("from_date")
        to_date = validated_query_params.get("to_date")

        transactions = TransactionService.get_transactions(from_date, to_date)

        if transactions:
            total_amount_in_SAR = transactions.aggregate(total_amount=Sum("amount"))["total_amount"]
            total_amount_in_USD = TransactionService.convert_currency(
                total_amount_in_SAR, SAR_TO_USD_RATE
            )
        else:
            total_amount_in_SAR = 0
            total_amount_in_USD = 0

        return Response(
            {
                "count": transactions.count(),
                "total_amount_in_SAR": total_amount_in_SAR,
                "total_amount_in_USD": total_amount_in_USD,
            }
        )
