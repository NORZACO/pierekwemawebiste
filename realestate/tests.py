from django.test import TestCase

from realestate.models.service import (
    Service,
    Icon,
    Properties,
    Agents,
    About,
    News,
    Testimonials,
    Contact,
)  # noqa: F811


# created tests
class ServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Service.objects.create(
            title="Test Service", description="Test Service Description"
        )

    def test_title_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_description_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_title_max_length(self):
        service = Service.objects.get(id=1)
        max_length = service._meta.get_field("title").max_length
        self.assertEquals(max_length, 100)

    def test_description_max_length(self):
        service = Service.objects.get(id=1)
        max_length = service._meta.get_field("description").max_length
        self.assertEquals(max_length, 1000)

    def test_object_name_is_title(self):
        service = Service.objects.get(id=1)
        expected_object_name = f"{service.title}"
        self.assertEquals(expected_object_name, str(service))

