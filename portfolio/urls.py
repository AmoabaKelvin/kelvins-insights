from django.urls import path

from . import views

urlpatterns = [
    path("", views.AboutView.as_view(), name="portfolio"),
    path("contact/", views.get_in_touch_view, name="get_in_touch"),
]
