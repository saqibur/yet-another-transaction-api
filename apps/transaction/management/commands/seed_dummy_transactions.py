# Standard library imports
from decimal import Decimal
from random import randrange, randint
from uuid import uuid4
from datetime import datetime

# Django imports
from django.core.management.base import BaseCommand

# Third part imports

# Local imports
from apps.transaction.models import Transaction
from common.decorators import restrict_to_development_environment


class Command(BaseCommand):
    help = "Creates dummy transactions"

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, nargs="?", default=1)

    @restrict_to_development_environment
    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        transactions = []

        for _ in range(count):
            transaction = Transaction(
                account_uuid=uuid4(),
                amount=Decimal(randrange(1, 15000)),
                transaction_datetime=datetime(
                    year=randint(2000, 2025), month=randint(1, 12), day=randint(1, 20)
                ),
            )
            transactions.append(transaction)
            self.stdout.write(
                self.style.SUCCESS(
                    f"Created transaction on {transaction.transaction_datetime} of {transaction.amount} SAR."
                )
            )

        Transaction.objects.bulk_create(transactions, 100)
