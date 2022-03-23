from django.contrib import admin
from .models import Product, Category, ProductReview, ProductComment

# Register your models here.
class ProductReviewAdmin(admin.ModelAdmin):
    model = ProductReview


class ProductCommentReviewAdmin(admin.ModelAdmin):
    model = ProductComment


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "rating",
        "image",
    )

    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(ProductReview, ProductReviewAdmin),
admin.site.register(ProductComment, ProductCommentReviewAdmin),

admin.site.register(Product, ProductAdmin),
admin.site.register(Category, CategoryAdmin)
