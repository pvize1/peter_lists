from django.db import models
from model_utils.models import TimeStampedModel


class Recipe(TimeStampedModel):
    name = models.CharField("Name of Recipe", max_length=255)
