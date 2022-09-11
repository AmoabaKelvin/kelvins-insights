from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from portfolio.models import Portfolio

from .models import BlogPost, NewsletterSubscribers
from .tasks import send_new_post_alert_to_users_in_newsletter, send_welcome_email


@receiver(post_save, sender=BlogPost)
def blog_post_created(sender, instance, created, **kwargs):
    """Sends a welcome email to a user who has just joined the newsletter"""
    if created:
        email_subject = "NEW BLOG POST"
        email_body = render_to_string(
            "blog/mails/blog_post_email.html", {"post": instance}
        )
        # check that there are emails present in the newsletter database table
        # before trying to send emails.
        # if not, then don't call the celery task to send any email.
        if not NewsletterSubscribers.objects.exists():
            pass
        else:
            emails_to_send_to = [i.email for i in NewsletterSubscribers.objects.all()]
            # Sending task to celery to send the emails in the background
            send_new_post_alert_to_users_in_newsletter.delay(
                emails_to_send_to, email_subject, email_body
            )


@receiver(post_save, sender=NewsletterSubscribers)
def newsletter_subscribed(sender, instance, created, **kwargs):
    """Sends a welcome email to a user who has just joined the newsletter"""
    if created:
        portfolio = Portfolio.objects.first()
        email_subject = "Welcome to my newsletter"
        email_body = render_to_string(
            "blog/mails/welcome_email.html", {"portfolio": portfolio}
        )
        to_email = instance.email
        # Sending task to celery to send the emails in the background
        send_welcome_email.delay(to_email, email_subject, email_body)
