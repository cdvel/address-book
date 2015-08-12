from django.test import TestCase
from contacts.models import Contact


class ContactTests(TestCase):

    def test_str(self):
        c = Contact(first_name='Kevin', last_name='Bacon')
        self.assertEqual(str(c), 'Kevin Bacon')
