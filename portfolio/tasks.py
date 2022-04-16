from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_message_to_myself(from_email: str, subject: str, message_content: str) -> None:
    """
    This task sends a message to myself after a user has submitted the contact
    me form.
    Args:
        from_email (str) : The email address of the user who submitted the form.
        subject (str) : The subject of the message.
        message_content (str) : The content of the message.
    """
    send_mail(
        subject=subject,
        message=message_content,
        from_email=from_email,
        recipient_list=[settings.EMAIL_HOST_USER],
    )
