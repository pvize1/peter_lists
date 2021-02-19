from django.db import models
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.urls import reverse


class Author(TimeStampedModel):
    name = models.CharField("Author Name", max_length=255)

    def __str__(self):
        return self.name

class BookType(TimeStampedModel):
    type = models.CharField("Book Type", max_length=25)

    def __str__(self):
        return self.type

class Publisher(TimeStampedModel):
    name = models.CharField("Book Publisher", max_length=255)

    def __str__(self):
        return self.name

class Book(TimeStampedModel):
    title = models.CharField("Book Title", max_length=255)
    subtitle = models.CharField("Subtitle", max_length=255, blank=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    description = models.TextField("Description", blank=True)
    isbn = models.CharField("ISBN Number", max_length=25, blank=True)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    pages = models.IntegerField("No. of Pages", default=0)
    type = models.ForeignKey("BookType", on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, default="_", blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if (not self.slug) or (self.slug == "_"):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
