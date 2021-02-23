from django.db import models
from model_utils.models import TimeStampedModel


class LegoSet(TimeStampedModel):
    name = models.CharField("Name of LEGO Set", max_length=255)
