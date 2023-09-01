# Standard library imports

# Django imports
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

# Third party imports

# Local imports
from apps.transaction.models import Transaction


class TransactionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
