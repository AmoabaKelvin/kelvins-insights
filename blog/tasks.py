from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_welcome_email(to_email: str, email_subject: str, email_body: str) -> None:
    """
    This task sends a welcome email to a user after they have registered for
    newsletter.
    Args:
        email_address (str) : The email address of the user who has registered.
        email_subject (str) : The subject of the email.
        email_body (str) : The content of the email in HTML format.
    """
    send_mail(
        subject=email_subject,
        message=email_body,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[to_email],
        html_message=email_body,
    )


@shared_task
def send_new_post_alert_to_users_in_newsletter(
    to_emails: list, email_subject, email_body
) -> None:
    """
    This task sends a notification to the users when a new post is published.
    Args:
        to_emails (list) : The list email addresses to send the email to.
        email_subject (str) : The subject of the email.
        email_body (str) : The content of the email in HTML format.
    """
    # currently, the email addresses in the to_emails are looped over and
    # for every single one, an email is sent to the user.
    for i in to_emails:
        send_mail(
            subject=email_subject,
            message=email_body,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[i],
            html_message=email_body,
        )
