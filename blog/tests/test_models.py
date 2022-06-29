from django.contrib.auth.models import User
from django.test import TestCase

from ..models import BlogPost, BlogComments, BlogLikes


class TestBlogModel(TestCase):
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
        self.comment = BlogComments.objects.create(
            blog=self.blog,
            name="Test User",
            body="This is a test comment.",
        )
        self.like = BlogLikes.objects.create(post=self.blog, ip_address="127.0.0.1")

    def test_blog_was_created(self):
        """Test that the blog was created."""
        self.assertIsInstance(self.blog, BlogPost)

    def test_blog_model_str(self):
        """Test that the blog model returns the correct string."""
        self.assertEqual(str(self.blog), "Test Blog")

    def test_blog_model(self):
        self.assertEqual(self.blog.author, self.user)
        self.assertEqual(self.blog.title, "Test Blog")
        self.assertEqual(self.blog.body, "This is a test blog.")
        self.assertEqual(self.blog.slug, "test-blog")
        self.assertEqual(self.blog.time_to_read, 5)

    # Tests for the Blog Comment model
    def test_blog_comment_model_str(self):
        """Test that the blog comment model returns the correct string."""
        self.assertEqual(str(self.comment), "This is a test comment.")

    def test_comment_belongs_to_blog(self):
        self.assertEqual(self.comment.blog, self.blog)

    def test_blog_comment_model(self):
        self.assertEqual(self.comment.name, "Test User")
        self.assertEqual(self.comment.body, "This is a test comment.")

    # Tests for the Like model
    def test_like_model_str(self):
        """Test that the like model returns the correct string."""
        self.assertEqual(str(self.like), f"{self.blog} - {self.like.ip_address}")

    def test_like_was_successfully_added_to_post(self):
        self.assertEqual(self.blog.likes.count(), 1)
