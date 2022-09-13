from ckeditor.fields import RichTextField
from django.db import models


class Portfolio(models.Model):
    """Model definition for Portfolio."""

    # PERSONAL
    intro = models.TextField()  # This is the intro paragraph on the about page
    description = RichTextField()
    profile_picture = models.ImageField(upload_to="media/myimages/", blank=True)

    # RESUME
    resume = models.FileField(upload_to="media/files/resume/", blank=True)

    # Social Media Handles
    github = models.URLField(max_length=200)
    linkedin = models.URLField(max_length=200)
    telegram = models.URLField(max_length=200)
    quora = models.URLField(max_length=200)
    twitter = models.URLField(max_length=200)

    # EDIT DATE
    edit_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Portfolio."""

        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio"

    def __str__(self):
        """Unicode representation of Portfolio."""
        return self.edit_date.strftime("%d/%m/%Y")
