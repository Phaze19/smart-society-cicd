from django.test import TestCase
from .models import Resident, Notice

class SmartSocietyTests(TestCase):
    def test_resident_creation(self):
        """Test Resident model creation and string representation."""
        resident = Resident.objects.create(
            name="Anurag Vedak",
            flat_number="A-101",
            contact="9876543210"
        )
        self.assertEqual(str(resident), "Anurag Vedak (A-101)")
        self.assertEqual(resident.flat_number, "A-101")

    def test_notice_creation(self):
        """Test Notice model creation and string representation."""
        notice = Notice.objects.create(
            title="Annual General Meeting",
            description="Discussion on society maintenance and amenities."
        )
        self.assertEqual(str(notice), "Annual General Meeting")

    def test_index_page(self):
        """Test home page response."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Smart Society")
