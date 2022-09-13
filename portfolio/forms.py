from django import forms


class GetInTouch(forms.Form):
    """This form will be used to send private messages to my email"""

    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "First Name", "class": "form-input"}
        ),
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-input"}),
    )
    email_address = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"placeholder": "Email Address", "class": "form-input form-email"}
        ),
    )
    subject = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"placeholder": "Subject", "class": "form-input form-subject"}
        ),
    )
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={"placeholder": "Message", "class": "form-input message-area"}
        ),
    )

    class Meta:
        # Add classes to the form fields
        widgets = {
            "email_address": forms.TextInput(
                attrs={"class": "form-input", "placeholder": "Email Address"}
            ),
            "subject": forms.TextInput(attrs={"class": "form-input"}),
            "message": forms.Textarea(attrs={"class": "form-input form-textarea"}),
        }
