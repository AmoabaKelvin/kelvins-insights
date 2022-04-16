from django.contrib import messages
from django.http import HttpResponseBadRequest, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView
from portfolio.models import Portfolio

from .forms import BlogCommentForm
from .models import BlogLikes, BlogPost, NewsletterSubscribers
from .utils import get_client_ip


class ListBlogPosts(ListView):
    model = BlogPost
    template_name = "blog/index.html"
    paginate_by = 30
    ordering = "-date_added"

    def get_context_object_name(self, object_list):
        return "blogs"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["portfolio"] = Portfolio.objects.first()
        return context


class BlogDetailView(View):
    """
    Detail view for blog comment, the blog is obtained using the slug.
    """

    def get(self, request, *args, **kwargs):
        blog = get_object_or_404(BlogPost, slug=kwargs["slug"])
        form = BlogCommentForm()
        self.portfolio = Portfolio.objects.first()
        self.ip_addresses = [i.ip_address for i in BlogLikes.objects.filter(post=blog)]
        return render(
            request,
            "blog/blog-post.html",
            {
                "form": form,
                "blog": blog,
                "portfolio": self.portfolio,
                "address": self.ip_addresses,
            },
        )

    def post(self, request, *args, **kwargs):
        form = BlogCommentForm(request.POST)
        blog = get_object_or_404(BlogPost, slug=kwargs["slug"])
        if form.is_valid():
            form.save(commit=False)
            form.instance.blog = blog
            form.save()
            return redirect(request.path)
        else:
            return HttpResponseBadRequest("Invalid form data")


def add_user_to_newsletter(request):
    """
    Add user to newsletter subscription
    """
    if request.method == "POST":
        email = request.POST.get("semail")
        if email:
            # process the obtained email address by checking t
            # if it already exists in the database before adding it.
            # If it does, then no need to add it again, so we
            # return an alert indicating that its already present.
            # If it doesn't, then we add it to the database and return a
            # success alert, redirecting the user to the previous screen.
            if NewsletterSubscribers.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                print(request.path)
                return redirect(request.META.get("HTTP_REFERER", "/"))
            else:
                NewsletterSubscribers.objects.create(email=email)
                messages.success(
                    request,
                    "Email added to newsletter. You will be notified when new posts are published.",
                )
                return redirect(request.META.get("HTTP_REFERER", "/"))
    return render(request, "blog/index.html")


@csrf_exempt
def like_a_blog_post(request, post_id):
    """
    This view handles the upvote of a blog post.
    """
    if request.method == "POST":
        post = get_object_or_404(BlogPost, id=post_id)
        ip_address = get_client_ip(request)
        if BlogLikes.objects.filter(post=post, ip_address=ip_address).exists():
            # Since the user has already liked the post, we need to
            # remove the like from the database.
            BlogLikes.objects.get(post=post, ip_address=ip_address).delete()
            return JsonResponse({"added": False, "likes": post.likes.count()})
        else:
            BlogLikes.objects.create(post=post, ip_address=ip_address)
            return JsonResponse(
                {
                    "added": True,
                    "likes": post.likes.count(),
                }
            )
    return HttpResponseBadRequest("Invalid request")


@require_http_methods(["GET"])
def search_blog_posts(request):
    """
    This view handles the search of blog posts.
    """
    # The name of the HTML input widget is called `search`
    # For now, the user's keyword is searched against the title of the blogs
    # present in the database.
    search_term = request.GET["search"]
    if search_term:
        # We need to search the database for the search term
        # and return the results.
        results = BlogPost.objects.filter(title__icontains=search_term)
        portfolio = Portfolio.objects.first()
        return render(
            request,
            "blog/search-results.html",
            {"blogs": results, "search_term": search_term, "portfolio": portfolio},
        )
    else:
        messages.error(request, "Please enter a search term.")
        return redirect("index")
