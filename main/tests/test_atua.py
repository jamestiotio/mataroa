from django.conf import settings
from django.test import TestCase
from django.urls import reverse

from main import models


class AtuaAnonTestCase(TestCase):
    def test_atua_users_get(self):
        response = self.client.get(reverse("atua_users_premium"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_grandfather"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_staff"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_active"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_active_nonnew"))
        self.assertEqual(response.status_code, 404)

    def test_atua_users_post(self):
        response = self.client.post(reverse("atua_users_premium"))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse("atua_users_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse("atua_users_grandfather"))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse("atua_users_staff"))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse("atua_users_active"))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse("atua_users_active_nonnew"))
        self.assertEqual(response.status_code, 404)

    def test_atua_posts_get(self):
        response = self.client.get(reverse("atua_posts_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_posts_recently"))
        self.assertEqual(response.status_code, 404)

    def test_atua_posts_post(self):
        response = self.client.post(reverse("atua_posts_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse("atua_posts_recently"))
        self.assertEqual(response.status_code, 404)

    def test_atua_pages_get(self):
        response = self.client.get(reverse("atua_pages_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_pages_recently"))
        self.assertEqual(response.status_code, 404)

    def test_atua_pages_post(self):
        response = self.client.post(reverse("atua_pages_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.post(reverse("atua_pages_recently"))
        self.assertEqual(response.status_code, 404)

    def test_atua_comments_get(self):
        response = self.client.get(reverse("atua_comments"))
        self.assertEqual(response.status_code, 404)

    def test_atua_comments_post(self):
        response = self.client.post(reverse("atua_comments"))
        self.assertEqual(response.status_code, 404)


class AtuaNonadminTestCase(TestCase):
    def setUp(self):
        self.user = models.User.objects.create(username="alice")
        self.client.force_login(self.user)

    def test_atua_users_nonadmin(self):
        response = self.client.get(reverse("atua_users_premium"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_grandfather"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_staff"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_active"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_users_active_nonnew"))
        self.assertEqual(response.status_code, 404)

    def test_atua_posts_nonadmin(self):
        response = self.client.get(reverse("atua_posts_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_posts_recently"))
        self.assertEqual(response.status_code, 404)

    def test_atua_pages_nonadmin(self):
        response = self.client.get(reverse("atua_pages_new"))
        self.assertEqual(response.status_code, 404)
        response = self.client.get(reverse("atua_pages_recently"))
        self.assertEqual(response.status_code, 404)

    def test_atua_comments_nonadmin(self):
        response = self.client.get(reverse("atua_comments"))
        self.assertEqual(response.status_code, 404)


class AtuaAdminTestCase(TestCase):
    def setUp(self):
        self.user = models.User.objects.create(username="alice", is_superuser=True)
        self.client.force_login(self.user)

    def test_atua_users_admin(self):
        response = self.client.get(reverse("atua_users_premium"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("atua_users_new"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("atua_users_grandfather"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("atua_users_staff"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("atua_users_active"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("atua_users_active_nonnew"))
        self.assertEqual(response.status_code, 200)

    def test_atua_posts_admin(self):
        response = self.client.get(reverse("atua_posts_new"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("atua_posts_recently"))
        self.assertEqual(response.status_code, 200)

    def test_atua_pages_admin(self):
        response = self.client.get(reverse("atua_pages_new"))
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse("atua_pages_recently"))
        self.assertEqual(response.status_code, 200)

    def test_atua_comments_admin(self):
        response = self.client.get(reverse("atua_comments"))
        self.assertEqual(response.status_code, 200)


class AtuaCommentsTestCase(TestCase):
    def setUp(self):
        self.admin = models.User.objects.create(username="alice", is_superuser=True)
        self.user = models.User.objects.create(username="bob", comments_on=True)
        self.post = models.Post.objects.create(
            owner=self.user,
            title="Welcome post",
            slug="welcome-post",
            body="Content sentence.",
            published_at="2020-02-06",
        )
        self.client.force_login(self.user)

    def test_comment_list(self):
        data = {
            "name": "Jon",
            "email": "jon@wick.com",
            "body": "Comment here.",
        }
        response = self.client.post(
            reverse("comment_create", args=(self.post.slug,)),
            HTTP_HOST=f"{self.user.username}.{settings.CANONICAL_HOST}",
            data=data,
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(models.Comment.objects.all().count(), 1)
        self.assertEqual(models.Comment.objects.all().first().name, data["name"])
        self.assertEqual(models.Comment.objects.all().first().email, data["email"])
        self.assertEqual(models.Comment.objects.all().first().body, data["body"])
        self.assertEqual(models.Comment.objects.all().first().post, self.post)
        self.assertEqual(models.Comment.objects.all().first().is_approved, False)
