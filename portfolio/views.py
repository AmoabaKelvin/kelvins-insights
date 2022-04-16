from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import GetInTouch
from .models import Portfolio
from .tasks import send_message_to_myself


def portfolio(request):
    """Renders the portfolio page."""
    portfolio = Portfolio.objects.first()
    return render(request, "portfolio/portfolio.html", {"portfolio": portfolio})


def get_in_touch_view(request):
    """
    This view handles the get in touch form.
    It takes the form data and sends an email to the admin(me).
    """
    portfolio = Portfolio.objects.first()
    if request.method == "POST":
        form = GetInTouch(request.POST)
        if form.is_valid():
            from_email = form.cleaned_data["email_address"]
            subject = form.cleaned_data["subject"]
            message = form.cleaned_data["message"]
            # Call the celery task to send message to myself
            send_message_to_myself.delay(from_email, subject, message)
            messages.success(
                request,
                "Thank you for reaching out to me. I will get back to you soon.",
            )
            return redirect(request.META.get("HTTP_REFERER"))
    else:
        form = GetInTouch()
    return render(
        request, "portfolio/get-in-touch.html", {"form": form, "portfolio": portfolio}
    )
