from django.db import models
from model_utils.models import TimeStampedModel
from django.conf import settings
from django.template.defaultfilters import slugify

# Create your models here.
class Image(TimeStampedModel):
    title = models.CharField("Image Title", max_length=200)
    slug = models.SlugField(unique=True, blank=False, default="_", max_length=200)
    url = models.URLField("URL", default="", blank=True, null=True)
    image = models.ImageField(upload_to="images/%Y/%m/%d/")
    description = models.TextField("Description", blank=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="image_created_by",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if (not self.slug) or (self.slug == "_"):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
