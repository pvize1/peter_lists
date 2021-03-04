from django.db import models
from model_utils.models import TimeStampedModel
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from ..books.models import Book


class Foodstuff(TimeStampedModel):
    name = models.CharField("Name", max_length=250)

    def __str__(self):
        return self.name


class Ingredient(TimeStampedModel):
    class FormChoices(models.TextChoices):
        TINNED = "TIN", _("Tinned")
        FROZEN = "FRZ", _("Frozen")
        FRESH = "FRS", _("Fresh")
        RAW = "RAW", _("Raw")
        COOKED = "CKD", _("Cooked")
        PORTION = "POR", _("Portion")
        CHOPPED = "CHP", _("Chopped")
        DICED = "DCD", _("Diced")
        SLICED = "SLC", _("Sliced")
        MELTED = "MLT", _("Melted")
        NONE = "NON", _("_")

    name = models.CharField("Ingredient", max_length=250, blank=True, default="_")
    foodstuff = models.ForeignKey("Foodstuff", on_delete=models.CASCADE)
    form = models.CharField(
        "Form",
        max_length=3,
        choices=FormChoices.choices,
        default=FormChoices.NONE,
    )

    def __str__(self):
        return self.name


class IngredientList(TimeStampedModel):
    class UomChoices(models.TextChoices):
        GRAM = "GRM", _("Gram")
        KILO = "KGM", _("Kilogram")
        MILLILITRE = "MLT", _("Millilitre")
        LITRE = "LTR", _("Litre")
        TSP = "TSP", _("Tea Spoon")
        TBSP = "TBS", _("Table Spoon")
        DSP = "DSP", _("Dessert Spoon")
        UNIT = "UNT", _("Unit")
        PORTION = "POR", _("Portion")
        SPLASH = "SPL", _("Splash")
        TASTE = "TST", _("To Taste")
        HANDFULL = "HND", _("Handful")
        NONE = "NON", _("_")

    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    ingredient = models.ForeignKey("Ingredient", on_delete=models.CASCADE)
    qty = models.DecimalField("Quantity", max_digits=5, decimal_places=2)
    uom = models.CharField(
        "Unit of Measure",
        max_length=3,
        choices=UomChoices.choices,
        default=UomChoices.NONE,
    )

    def __str__(self):
        return self.ingredient.foodstuff.name


class Recipe(TimeStampedModel):
    title = models.CharField("Name of Recipe", max_length=250)
    description = models.TextField("Description", blank=True)
    method = models.TextField("Method", blank=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through=IngredientList,
        related_name="ingredient",
    )
    tag = models.CharField("Tag", max_length=100, blank=True, default="none, ")
    serves = models.IntegerField("Serves", default=0)
    prep = models.DecimalField("Prep (hrs)", max_digits=5, decimal_places=2, default=0)
    cook = models.DecimalField("Cook (hrs)", max_digits=5, decimal_places=2, default=0)
    slug = models.SlugField(unique=True, default="_", blank=False)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):  # new
        if (not self.slug) or (self.slug == "_"):
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class CookBookList(TimeStampedModel):
    cookbook = models.ForeignKey("books.Book", on_delete=models.CASCADE)
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    page = models.IntegerField("Page No.", default=0)
    url = models.URLField("URL", default="_")

    def __str__(self):
        return f"{self.cookbook.title}; {self.recipe.title}"
