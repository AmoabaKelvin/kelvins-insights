from autoslug import AutoSlugField
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager

from .utils import calculate_time_to_read


class BlogPost(models.Model):
    """Model for Blog Posts"""

    # Choose the default first person in the database to use and assign it
    # to the author
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=255, unique=True)
    body = RichTextField(config_name="default")
    slug = AutoSlugField(populate_from="title", unique=True)
    tags = TaggableManager()
    post_image = models.ImageField(upload_to="media/blog_images", blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    time_to_read = models.PositiveIntegerField(default=0, blank=True)

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs) -> None:
        self.time_to_read = calculate_time_to_read(self.body)
        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})

    def get_full_absolute_url(self):
        return f"{Site.objects.get_current().domain}{self.get_absolute_url()}"


# This model handles everything related to the newsletter. It's from
# this list that notifications will be sent to users about new
# articles who have subscribed to receive it.
# Also, it wll be used to send weekly digests to the various users
# that have subscribed to the newsletter.
# The url for newsletter subscription is /newsletter/subscribe/
class NewsletterSubscribers(models.Model):
    """Model for Newsletter Subscribers"""

    email = models.EmailField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Newsletter Subscribers"

    def __str__(self):
        return self.email


class BlogLikes(models.Model):
    """Allow user to upvote a blog post"""

    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name="likes")
    ip_address = models.GenericIPAddressField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blog Likes"

    def __str__(self):
        return f"{self.post} - {self.ip_address}"
