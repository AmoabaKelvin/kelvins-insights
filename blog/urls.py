from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListBlogPosts.as_view(), name="index"),
    path("blog/<slug:slug>", views.BlogDetailView.as_view(), name="detail"),
    path("newsletter/", views.NewsletterView.as_view(), name="newsletter"),
    path("like/<int:post_id>", views.like_a_blog_post, name="like_a_blog_post"),
    path("search/", views.BlogSearchView.as_view(), name="search"),
]
