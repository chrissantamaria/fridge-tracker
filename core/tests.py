from django.test import TestCase
from .models import Item
from django.contrib.auth.models import User


class ItemTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(
            username='james', password='very_secure')
        Item.objects.create(name='Eggs', owner=user)
        Item.objects.create(name='Cheese', owner=user)

    def test_number_of_items(self):
        print(Item.objects.all())
        self.assertEqual(Item.objects.all().count(), 2)

    def test_item_str_representation(self):
        eggs = Item.objects.get(name='Eggs')
        cheese = Item.objects.get(name='Cheese')

        self.assertEqual(str(eggs), 'Eggs')
        self.assertEqual(str(cheese), 'Cheese')
