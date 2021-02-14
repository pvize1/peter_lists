from django.db import models
from model_utils.models import TimeStampedModel


class Book(TimeStampedModel):
    title = models.CharField("Title of Book", max_length=255)
