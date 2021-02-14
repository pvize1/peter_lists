from django.db import models
from model_utils.models import TimeStampedModel


class OrigamiModel(TimeStampedModel):
    name = models.CharField("Name of Origami Model", max_length=255)
