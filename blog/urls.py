from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListBlogPosts.as_view(), name="index"),
    path("blog/<slug:slug>", views.BlogDetailView.as_view(), name="detail"),
    path("newsletter/", views.add_user_to_newsletter, name="newsletter"),
    path("like/<int:post_id>", views.like_a_blog_post, name="like_a_blog_post"),
    path("search/", views.search_blog_posts, name="search"),
]
