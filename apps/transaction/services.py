# Standard library imports
from datetime import (
    date,
    timedelta,
)
from decimal import Decimal

# Django imports
from django.utils import timezone
from rest_framework.exceptions import ValidationError

# Third party imports

# Local imports
from apps.transaction.models import Transaction


class TransactionService:
    @staticmethod
    def get_transactions(
        from_date: date = timezone.now() - timedelta(days=30.0),
        to_date: date = timezone.now(),
    ):
        if to_date - from_date > timedelta(days=365):
            raise ValidationError("The time range cannot be higher than 1 year")

        return Transaction.objects.filter(
            transaction_datetime__date__gte=from_date,
            transaction_datetime__date__lte=to_date,
        ).order_by("transaction_datetime")

    @staticmethod
    def convert_currency(
        amount: Decimal,
        conversion_rate: float,
    ):
        return amount * Decimal(conversion_rate)
