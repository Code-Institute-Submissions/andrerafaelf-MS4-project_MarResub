from audioop import avg
from xml.etree.ElementTree import Comment
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Sum, Count, Avg, F
from django.db.models.functions import Lower, Coalesce

from .models import Product, Category, ProductComment, ProductReview
from .forms import ProductForm, ProducReviewtForm

# Create your views here.


def all_products(request):
    """A view to show all products, including sorting and search queries"""

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if "sort" in request.GET:
            sortkey = request.GET["sort"]
            sort = sortkey
            if sortkey == "name":
                sortkey = "lower_name"
                products = products.annotate(lower_name=Lower("name"))
            if sortkey == "category":
                sortkey = "category__name"
            if "direction" in request.GET:
                direction = request.GET["direction"]
                if direction == "desc":
                    sortkey = f"-{sortkey}"
            products = products.order_by(sortkey)

        if "category" in request.GET:
            categories = request.GET["category"].split(",")
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if "q" in request.GET:
            query = request.GET["q"]
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse("products"))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    products = products.annotate(
        total_stars=Sum("reviews__stars"), total_reviews=Count("reviews")
    ).annotate(star_rating=F("total_stars") / F("total_reviews"))

    current_sorting = f"{sort}_{direction}"

    context = {
        "products": products,
        "search_term": query,
        "current_categories": categories,
        "current_sorting": current_sorting,
    }

    return render(request, "products/products.html", context)


def product_detail(request, product_id):
    """A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    user_can_post_review = False
    review_form = None
    ## rating evaluation statistics
    total_reviews = product.reviews.count()
    total_stars = product.reviews.aggregate(stars=Coalesce(Sum("stars"), 0))["stars"]
    if total_reviews:
        avg_stars = total_stars / total_reviews
    else:
        avg_stars = 0

    if request.user.is_authenticated:
        # check if user doesn't have any previouse reviews and comments
        # on this product
        if not product.reviews.filter(user=request.user).exists():
            user_can_post_review = True  # this mean user doesn't have previouse reviews
            review_form = ProducReviewtForm()
    else:
        user_can_post_review = False
    context = {
        "product": product,
        "review_form": review_form,
        "user_can_post_review": user_can_post_review,
        "total_reviews": total_reviews,
        "star_rating": avg_stars,
    }

    ## check if request method is post method
    if request.method == "POST":
        if user_can_post_review and request.POST.get("review", None) == "post-review":
            form = ProducReviewtForm(data=request.POST)
            if form.is_valid():
                print("form is valid", form)
                comment_input = request.POST.get("comment", "")
                stars_input = form.cleaned_data.get("stars", 0)
                review = ProductReview(
                    user=request.user, product=product, stars=stars_input
                )
                review.save()
                comment = ProductComment(
                    review=review,
                    user=request.user,
                    product=product,
                    comment=comment_input,
                )
                comment.save()
                context["review_form"] = None
                return render(request, "products/product_detail.html", context)
            else:
                print(form.errors)
                context["review_form"] = form
                context["user_can_post_review"] = False
                return render(request, "products/product_detail.html", context)

        else:
            return render(request, "products/product_detail.html", context)

    return render(request, "products/product_detail.html", context)


@login_required
def add_product(request):
    """Add a product to the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, "Successfully added product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to add product. Please ensure the form is valid."
            )
    else:
        form = ProductForm()

    template = "products/add_product.html"
    context = {
        "form": form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully updated product!")
            return redirect(reverse("product_detail", args=[product.id]))
        else:
            messages.error(
                request, "Failed to update product. Please ensure the form is valid."
            )
    else:
        form = ProductForm(instance=product)
        messages.info(request, f"You are editing {product.name}")

    template = "products/edit_product.html"
    context = {
        "form": form,
        "product": product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, "Sorry, only store owners can do that.")
        return redirect(reverse("home"))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, "Product deleted!")
    return redirect(reverse("products"))
