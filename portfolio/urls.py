from django.urls import path

from . import views

urlpatterns = [
    path("", views.portfolio, name="portfolio"),
    path("contact/", views.get_in_touch_view, name="get_in_touch"),
]
