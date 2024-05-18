from django.test import TestCase
from .models import Ttj

class TtjModelTest(TestCase):

    def setUp(self):
        # Set up a sample Ttj instance
        self.ttj = Ttj.objects.create(
            name="Example Dormitory",
            university="Example University",
            address="123 Example Street"
        )

    def test_ttj_creation(self):
        # Test if the Ttj instance is created correctly
        self.assertIsInstance(self.ttj, Ttj)
        self.assertEqual(self.ttj.name, "Example Dormitory")
        self.assertEqual(self.ttj.university, "Example University")
        self.assertEqual(self.ttj.address, "123 Example Street")
        self.assertIsNotNone(self.ttj.created_at)

    def test_ttj_str_method(self):
        # Test the __str__ method of the Ttj model
        self.assertEqual(str(self.ttj), "Example Dormitory")

    def test_unique_name_constraint(self):
        # Test the unique constraint on the name field
        with self.assertRaises(Exception):
            Ttj.objects.create(
                name="Example Dormitory",  # Same name as the existing one
                university="Another University",
                address="456 Another Street"
            )

    def test_verbose_names(self):
        # Test the verbose_name and verbose_name_plural for the model
        self.assertEqual(Ttj._meta.verbose_name, "Talabalar turar joyi")
        self.assertEqual(Ttj._meta.verbose_name_plural, "Talabalar turar joylari")

