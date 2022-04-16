from django import forms

from .models import BlogComments


class BlogCommentForm(forms.ModelForm):
    """Form definition for BlogComment."""

    class Meta:
        """Meta definition for BlogCommentform."""

        model = BlogComments
        fields = ("name", "body")
        widgets = {
            "name": forms.TextInput(
                attrs={"placeholder": "Name", "class": "form-control", "id": "name"}
            ),
            "body": forms.Textarea(
                attrs={"placeholder": "Comment", "class": "form-control", "rows": "3"}
            ),
        }
