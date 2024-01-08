from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Post, Restaurant


class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername12",
            password="myPassword23",
            email="test@test.com"
        )
        self.restaurant = Restaurant(name="XYZ", description="ABCD", address1="cvx", city="def", 
                                     county="fes", phone="564")
        self.restaurant.save()
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1, restaurant=self.restaurant)
        self.post.save()

    def test_render_post_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'post_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)