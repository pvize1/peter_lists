from django.db import models
from model_utils.models import TimeStampedModel
from django.urls import reverse


# Create your models here.
class Blog(TimeStampedModel):
    title = models.CharField("Title", max_length=250)
    description = models.TextField("Description", blank=True)
    date = models.DateTimeField("Date")
    tag = models.CharField("Tag", max_length=100, blank=True, default="none, ")

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:list")
