from django.db import models
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.urls import reverse


class Books(TimeStampedModel):
    pass


class Book(TimeStampedModel):
    title = models.CharField("Title of Book", max_length=255)
    subtitle = models.CharField("Subtitle of Book", max_length=255, blank=True)
    author = models.CharField("Author(s) of Book", max_length=255, blank=True)
    description = models.TextField("Description", blank=True)
    slug = models.SlugField(unique=True, default="_", blank=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if (not self.slug) or (self.slug == "_"):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
