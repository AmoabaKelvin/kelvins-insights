from ckeditor.fields import RichTextField
from django.db import models


class Portfolio(models.Model):
    """Model definition for Portfolio."""

    # PERSONAL
    short_description = models.CharField(max_length=500)
    long_description = models.TextField()
    profile_picture = models.ImageField(upload_to="media/myimages/", blank=True)

    # PORTFOLIO
    experience = RichTextField()
    projects = RichTextField()
    skills = RichTextField()
    education = RichTextField()

    # RESUME
    resume = models.FileField(upload_to="media/files/resume/", blank=True)

    # Social Media Handles
    github = models.URLField(max_length=200)
    linkdin = models.URLField(max_length=200)
    # reddit = models.URLField(max_length=200)
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
