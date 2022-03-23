from cProfile import label
from random import choices
from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, ProductReview


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields["category"].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"


class ProducReviewtForm(forms.Form):
    STARS_CHOICES = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    stars = forms.ChoiceField(choices=STARS_CHOICES, required=True)
    comment = forms.CharField(widget=forms.Textarea, required=True)

    def __init__(self, request=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["comment"].widget.attrs = {"rows": 3, "cols": "50"}
        # self.fields['comment'].label = ''
        for field_name, field in self.fields.items():
            if field.widget.attrs.get("class"):
                field.widget.attrs["class"] += " form-control"
            else:
                field.widget.attrs["class"] = "form-control"
