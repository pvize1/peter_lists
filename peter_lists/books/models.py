from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from django.urls import reverse


class Author(TimeStampedModel):
    name = models.CharField("Author Name", max_length=250)
    slug = models.SlugField(unique=True, default="_", blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:author_list")

    def save(self, *args, **kwargs):
        if (not self.slug) or (self.slug == "_"):
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class BookType(TimeStampedModel):
    type = models.CharField("Book Type", max_length=25)

    class Meta:
        ordering = ["type"]

    def __str__(self):
        return self.type

    def get_absolute_url(self):
        return reverse("books:booktype_list")


class Publisher(TimeStampedModel):
    name = models.CharField("Book Publisher", max_length=250)
    slug = models.SlugField(unique=True, default="_", blank=False)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("books:publishers_list")

    def save(self, *args, **kwargs):
        if (not self.slug) or (self.slug == "_"):
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class BookManager(models.Manager):
    def get_queryset(self):
        return super(BookManager, self).get_queryset().filter(type=3)

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
    tag = models.CharField("Tag", max_length=100, blank=True, default="none, ")
    rating = models.IntegerField("Rating (1-10)", default=0)
    pct_read = models.IntegerField("Pct% Read", default=0)

    class Meta:
        ordering = [
            "title",
            "subtitle",
        ]

    books = models.Manager()
    cook_books = BookManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:list")

    def save(self, *args, **kwargs):  # new
        if (not self.slug) or (self.slug == "_"):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
