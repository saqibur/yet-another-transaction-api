# Standard library imports
import uuid

# Django imports
from django.conf import settings
from django.db import models

# Third part imports

# Local imports


class BaseModel(models.Model):
    uuid = models.UUIDField(verbose_name="UUID", unique=True, default=uuid.uuid4, editable=False)

    # NOTE: For the purposes of this project, we're going to assume a "user"
    #       will simply be represented by a UUID passed to this micro-service.
    created_by = models.UUIDField(
        verbose_name="Created by UUID",
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True, editable=False)

    class Meta:
        abstract = True
