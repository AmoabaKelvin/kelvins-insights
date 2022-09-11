from django.contrib import admin

from .models import BlogLikes, BlogPost, NewsletterSubscribers


@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    """Admin View for Blog"""

    list_display = (
        "title",
        "date_added",
    )
    readonly_fields = ("time_to_read",)
    search_fields = ("title", "likes")
    ordering = ("-date_added",)


# @admin.register(BlogComments)
# class BlogCommentAdmin(admin.ModelAdmin):
#     """Admin View for BlogComment"""

#     list_display = ("name", "blog", "date_added")
#     list_filter = ("blog", "date_added")
#     search_fields = ("blog", "date_added")
#     ordering = ("-date_added",)


@admin.register(NewsletterSubscribers)
class NewsletterAdmin(admin.ModelAdmin):
    """Admin View for Newsletter"""

    list_display = ("email", "date_added")
    ordering = ("-date_added",)


@admin.register(BlogLikes)
class LikeAdmin(admin.ModelAdmin):
    """Admin View for Like"""

    list_display = ("ip_address", "date_added")
    ordering = ("-date_added",)
