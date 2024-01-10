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
        self.restaurant = Restaurant(name="Restaurant Name", description="Restaurant Description", 
                                     address1="address line 1", 
                                     city="city", 
                                     county="county", 
                                     phone="123456")
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

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername12", password="myPassword23")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'post_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )

    def test_render_restaurant_detail_page(self):
        response = self.client.get(reverse(
            'restaurant_detail', args=['blog-title', self.restaurant.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Restaurant Name", response.content)
        self.assertIn(b"Restaurant Description", response.content)
        self.assertIn(b"address line 1", response.content)
        self.assertIn(b"city", response.content)
        self.assertIn(b"county", response.content)
        self.assertIn(b"123456", response.content)