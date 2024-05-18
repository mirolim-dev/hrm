from django.test import TestCase
from .models import Ttj, Staff
from django.contrib.admin.sites import AdminSite
from django.test import TestCase
from django.contrib.auth.models import User
from .admin import StaffAdmin
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


class StaffModelTestCase(TestCase):

    def setUp(self):
        # Set up a sample staff instance with a salary value
        self.staff = Staff.objects.create(
            first_name="John",
            last_name="Doe",
            phone="123456789",
            salary=50000,  # Provide a salary value to satisfy the NOT NULL constraint
            ttj_id=Ttj.objects.create(name="Test Dormitory", university="Test University", address="Test Address"),
            role=1,
            is_working=True
        )

    def test_staff_creation(self):
        # Test the creation of the staff instance
        self.assertIsInstance(self.staff, Staff)
        # Add additional assertions as needed



class StaffAdminTestCase(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.staff_admin = StaffAdmin(Staff, self.site)

        # Create some sample staff instances
        Staff.objects.create(first_name="John", last_name="Doe", phone="123456789", is_working=True)
        Staff.objects.create(first_name="Jane", last_name="Doe", phone="987654321", is_working=False)

    def test_filter_is_working(self):
        request = self.client.get('/admin/yourappname/staff/')  # Replace 'yourappname' with your app name
        staff_working = self.staff_admin.get_queryset(Staff.objects.all()).filter(is_working=True)
        staff_not_working = self.staff_admin.get_queryset(Staff.objects.all()).filter(is_working=False)
        # staff_working = self.staff_admin.get_queryset(Staff.objects.all()).filter(is_working=True)


        self.assertEqual(staff_working.count(), 1)  # Assert only one staff is working
        self.assertEqual(staff_not_working.count(), 1)  # Assert only one staff is not working
