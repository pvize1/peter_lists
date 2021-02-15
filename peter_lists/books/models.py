from django.db import models
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.urls import reverse


class Book(TimeStampedModel):
    title = models.CharField("Title of Book", max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
