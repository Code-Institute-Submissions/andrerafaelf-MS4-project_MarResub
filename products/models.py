from email.policy import default
from itertools import product
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        "Category", null=True, blank=True, on_delete=models.SET_NULL
    )
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


# product reviews model
class ProductReview(models.Model):
    STARS_CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )

    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="reviews")
    stars = models.PositiveSmallIntegerField(
        verbose_name="stars", default=0, choices=STARS_CHOICES
    )
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)

    def __str__(self) -> str:
        try:
            return "Review:>>" + self.product.name
        except:
            pass


# product comment  models
class ProductComment(models.Model):
    review = models.OneToOneField(to=ProductReview, on_delete=models.CASCADE)
    product = models.ForeignKey(
        to=Product, on_delete=models.CASCADE, related_name="reviews_comments"
    )
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name="reviews_comments"
    )
    comment = models.CharField(
        verbose_name="comment", blank=False, max_length=400, null=False
    )
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
