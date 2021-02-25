from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse


class Author(TimeStampedModel):
    name = models.CharField("Author Name", max_length=250)

    def __str__(self):
        return self.name


class BookType(TimeStampedModel):
    type = models.CharField("Book Type", max_length=25)

    def __str__(self):
        return self.type


class Publisher(TimeStampedModel):
    name = models.CharField("Book Publisher", max_length=250)

    def __str__(self):
        return self.name


class Book(TimeStampedModel):
    class StatusChoices(models.TextChoices):
        COMPLETED = "RD", _("Completed")
        READING = "RG", _("Reading")
        TO_READ = "TR", _("To read")
        NEXT = "NT", _("Next")
        BROWSING = "BG", _("Browsing")
        REFERENCE = "RE", _("Reference")
        GIVEN_UP = "GU", _("Given-up")
        WISH_LIST = "WL", _("Wishlist")
        INACTIVE = "IA", _("Inactive")
        UNKOWN = "UK", _("Unknown")

    class FormChoices(models.TextChoices):
        PAPERBACK = "PB", _("Paperback")
        HARDBACK = "HB", _("Hardback")
        KINDLE = "KI", _("Kindle")
        MAGAZINE = "MA", _("Magazine")
        WISH_LIST = "WL", _("Wishlist")
        OTHER = "OT", _("Other")

    title = models.CharField("Book Title", max_length=250)
    subtitle = models.CharField("Subtitle", max_length=250, blank=True)
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    description = models.TextField("Description", blank=True)
    isbn = models.CharField("ISBN Number", max_length=25, blank=True)
    publisher = models.ForeignKey("Publisher", on_delete=models.CASCADE)
    pages = models.IntegerField("No. of Pages", default=0)
    type = models.ForeignKey("BookType", on_delete=models.CASCADE)
    form = models.CharField(
        "Form",
        max_length=2,
        choices=FormChoices.choices,
        default=FormChoices.OTHER,
    )
    status = models.CharField(
        "Status",
        max_length=2,
        choices=StatusChoices.choices,
        default=StatusChoices.UNKOWN,
    )
    slug = models.SlugField(unique=True, default="_", blank=False)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    rating = models.IntegerField("Rating (1-10)", default=0)
    pct_read = models.IntegerField("Pct% Read", default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if (not self.slug) or (self.slug == "_"):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
