from django.contrib import messages
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from portfolio.models import Portfolio

from .models import BlogLikes, BlogPost, NewsletterSubscribers
from .utils import get_client_ip


class ListBlogPosts(ListView):
    # get each of the blog posts from the database and prefetch their tags
    # and order them by the date they were added in descending order
    queryset = BlogPost.objects.prefetch_related("tags").order_by("-date_added")
    template_name = "blog/index-new.html"
    paginate_by = 30
    ordering = "-date_added"

    def get_context_object_name(self, object_list):
        return "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portfolio"] = Portfolio.objects.first()
        return context


class BlogDetailView(View):
    """Detail view for blog comment, the blog is obtained using the slug."""

    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(
            BlogPost.objects.prefetch_related("tags"), slug=kwargs["slug"]
        )
        self.ip_addresses = [i.ip_address for i in BlogLikes.objects.filter(post=blog)]
        return render(
            request,
            "blog/detail.html",
            {
                "blog": blog,
                "address": self.ip_addresses,
            },
        )


class NewsletterView(View):
    """
    View to handle the addition of an email to the list of newsletter
    substribers
    """

    def post(self, request, *args, **kwargs):
        homepage: str = reverse("index")
        email: str = request.POST.get("user_email")
        if email:
            if NewsletterSubscribers.objects.filter(email=email).exists():
                messages.error(request, "Email alread exists")
                return redirect(homepage)
            NewsletterSubscribers.objects.create(email=email)
            messages.success(
                request,
                "Thank you for subscribing to my newsletter, you will be the first to know when I publish a new blog post.",
            )
            return redirect(homepage)
        return render(request, "blog/index-new.html")


@csrf_exempt
def like_a_blog_post(request, post_id):
    """This view handles the upvote of a blog post."""
    if request.method == "POST":
        post = get_object_or_404(BlogPost, id=post_id)
        ip_address = get_client_ip(request)
        if BlogLikes.objects.filter(post=post, ip_address=ip_address).exists():
            # Since the user has already liked the post, we need to
            # remove the like from the database.
            BlogLikes.objects.get(post=post, ip_address=ip_address).delete()
            return JsonResponse({"added": False, "likes": post.likes.count()})
        BlogLikes.objects.create(post=post, ip_address=ip_address)
        return JsonResponse(
            {
                "added": True,
                "likes": post.likes.count(),
            }
        )
    return HttpResponseBadRequest("Invalid request")


class BlogSearchView(View):
    """
    Handle the searching of a blog post
    """

    def get(self, request, *args, **kwargs):
        search_term = request.GET["search"]
        results_queryset = BlogPost.objects.filter(title__icontains=search_term)
        return render(
            request,
            "blog/index-new.html",
            {
                "blogs": results_queryset,
                "search_term": search_term,
            },
        )
