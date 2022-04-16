from django import forms


class GetInTouch(forms.Form):
    """
    This form will be used to send private messages to my email
    """

    email_address = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
