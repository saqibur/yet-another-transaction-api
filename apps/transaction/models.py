# Standard library imports

# Django imports
from django.db import models

# Third party imports

# Local imports
from apps.core.models import BaseModel


class Transaction(BaseModel):
    account_uuid = models.UUIDField()

    # NOTE: This can be changed on demand. 12 is chosen arbitrarily for now.
    # NOTE: The amount is also treated as only SAR values.
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_datetime = models.DateTimeField()

    class Meta:
        unique_together = ("account_uuid", "amount", "transaction_datetime")
