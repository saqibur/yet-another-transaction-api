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
from common.constants import TRANSACTION_ALARM_TRIGGER_THRESHOLD


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

    @staticmethod
    def anomaly_check():
        # NOTE: We can add some kind of SMS/Email or system notification here,
        #       but for now we're just writing to the console.
        transactions = list(
            Transaction.objects.order_by("-id")[:TRANSACTION_ALARM_TRIGGER_THRESHOLD].values()
        )
        if transactions[-1]["created_at"] - transactions[0]["created_at"] < timedelta(hours=1):
            print("More than 5 transactions have occurred within an hour.")
