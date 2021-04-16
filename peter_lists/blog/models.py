from django.db import models
from model_utils.models import TimeStampedModel
from django.urls import reverse
from django.conf import settings
from ..images.models import Image


# Create your models here.
class ImageList(TimeStampedModel):
    order = models.IntegerField("Ord", default=0)
    blogs = models.ForeignKey("Blog", on_delete=models.CASCADE)
    blog_image = models.ForeignKey("images.Image", on_delete=models.CASCADE)

    def __str__(self):
        return self.blogs.title


class Blog(TimeStampedModel):
    title = models.CharField("Title", max_length=250)
    description = models.TextField("Description", blank=True)
    date = models.DateTimeField("Date")
    tag = models.CharField("Tag", max_length=100, blank=True, default="none, ")
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="blog_created_by",
        on_delete=models.CASCADE,
    )
    images = models.ManyToManyField(
        Image,
        through=ImageList,
        related_name="blog_image",
    )

    class Meta:
        ordering = ["-date", "title"]

    blog = models.Manager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:list")
