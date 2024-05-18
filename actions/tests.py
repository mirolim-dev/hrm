from django.test import TestCase

from staffs.models import Staff, Ttj
from .models import StaffLeaving
# Create your tests here.
class StaffLeavingModelTestCase(TestCase):

    def test_staff_leaving_creation(self):
        staff = Staff.objects.create(
            first_name="Jane",
            last_name="Doe",
            phone="987654321",
            ttj_id=Ttj.objects.create(name="Another Dormitory", university="Another University", address="Another Address"),
            role=2,
            is_working=True
        )
        reason = "Moving to another city"
        staff_leaving = StaffLeaving.objects.create(staff_id=staff, reason=reason)
        self.assertIsInstance(staff_leaving, StaffLeaving)
        self.assertEqual(staff_leaving.staff_id, staff)
        self.assertEqual(staff_leaving.reason, reason)
        self.assertIsNotNone(staff_leaving.left_at)


class SignalTestCase(TestCase):

    def test_staff_leaving_signal_handler(self):
        staff = Staff.objects.create(
            first_name="Jane",
            last_name="Doe",
            phone="987654321",
            ttj_id=Ttj.objects.create(name="Another Dormitory", university="Another University", address="Another Address"),
            role=2,
            is_working=True
        )

        staff_leaving = StaffLeaving.objects.create(staff_id=staff, reason="Moving to another city")

        staff.refresh_from_db()  # Refresh staff instance from database
        self.assertFalse(staff.is_working)
