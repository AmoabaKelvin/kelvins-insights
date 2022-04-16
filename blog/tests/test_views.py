from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from ..models import BlogPost


class TestBlogViews(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="test_user",
            password="test_password",
        )
        self.blog = BlogPost.objects.create(
            author=self.user,
            title="Test Blog",
            body="This is a test blog.",
        )
        self.client = Client()

    def test_blog_list_view(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/index.html")

    def test_blog_detail_view(self):
        response = self.client.get(reverse("detail", args=[self.blog.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/blog-post.html")

    # def test_blog_comment_view(self):
    #     response = self.client.get(reverse("blog:comment", args=[self.blog.url]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, "blog/blog_comment.html")

    def test_blog_comment_post_view_with_invalid_data(self):
        response = self.client.post(
            reverse("detail", args=[self.blog.slug]),
            {"name": "", "body": "This is a test comment."},
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(self.blog.likes.count(), 0)

    def test_blog_comment_post_view_with_valid_data(self):
        response = self.client.post(
            reverse("detail", args=[self.blog.slug]),
            {"name": "Test User", "body": "This is a test comment."},
        )
        self.assertEqual(response.status_code, 302)
