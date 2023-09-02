# Standard library imports

# Django imports
from rest_framework import serializers

# Third party imports

# Local imports
from apps.transaction.models import Transaction


class TransactionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"


class ReportDateRangeSerializer(serializers.Serializer):
    to_date = serializers.DateField(required=True)
    from_date = serializers.DateField(required=True)
