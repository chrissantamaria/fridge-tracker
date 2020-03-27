from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client


class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='chris', password='hunter2')
        user = User.objects.create_user(username='david', password='password')

    def test_number_of_users(self):
        print(User.objects.all())
        self.assertEqual(User.objects.all().count(), 2)

    def test_can_authenticate_user(self):
        c = Client()
        self.assertTrue(c.login(username='chris', password='hunter2'))

    def test_invalid_password(self):
        c = Client()
        self.assertFalse(c.login(username='chris', password='not_hunter2'))
