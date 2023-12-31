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


class IconTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Icon.objects.create(icon_class="Test Icon")

    def test_icon_class_label(self):
        icon = Icon.objects.get(icon_class="Test Icon")
        field_label = icon._meta.get_field("icon_class").verbose_name
        self.assertEquals(field_label, "icon class")

    def test_icon_class_max_length(self):
        icon = Icon.objects.get(icon_class="Test Icon")
        max_length = icon._meta.get_field("icon_class").max_length
        self.assertEquals(max_length, 255)

    def test_object_name_is_icon_class(self):
        icon = Icon.objects.get(icon_class="Test Icon")
        expected_object_name = f"{icon.icon_class}"
        self.assertEquals(expected_object_name, str(icon))
        

class ServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        icon = Icon.objects.create(icon_class="Test Icon")
        Service.objects.create(icon=icon, title="Test Title", description="Test Description")

    def test_title_label(self):
        service = Service.objects.get(id=1)
        field_label = service._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_title_max_length(self):
        service = Service.objects.get(id=1)
        max_length = service._meta.get_field("title").max_length
        self.assertEquals(max_length, 50)

    def test_object_name_is_title(self):
        service = Service.objects.get(id=1)
        expected_object_name = f"{service.title}"
        self.assertEquals(expected_object_name, str(service))

    def test_get_icon(self):
        service = Service.objects.get(id=1)
        expected_icon = f"{service.icon.icon_class}"
        self.assertEquals(expected_icon, service.get_icon())
        
        
    # functions of pages
    def test_get_services(self):
        response = self.client.get("/property_grid")
        self.assertEqual(response.status_code, 200)
        
    def test_get_properties(self):
        response = self.client.get("/contact")
        self.assertEqual(response.status_code, 200)
    
    def test_get_about(self):
        response = self.client.get("/about")
        self.assertEqual(response.status_code, 200)
        
    def test_get_news(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)


class PropertiesTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Properties.objects.create(
            title="Test Title",
            description="Test Description",
            price=100,
            location="Test Location",
            street_address="Test Street Address",
            bedroom=1,
            bathroom=1,
            garage=1,
            area=1,
            property_type="Test Property Type",
            status="Test Status",
            
        )

    def test_title_label(self):
        properties = Properties.objects.get(id=1)
        field_label = properties._meta.get_field("title").verbose_name
        self.assertEquals(field_label, "title")

    def test_title_max_length(self):
        properties = Properties.objects.get(id=1)
        max_length = properties._meta.get_field("title").max_length
        self.assertEquals(max_length, 100)

    def test_object_name_is_title(self):
        properties = Properties.objects.get(id=1)
        expected_object_name = f"{properties.title}"
        self.assertEquals(expected_object_name, str(properties))

    def test_description_label(self):
        properties = Properties.objects.get(id=1)
        field_label = properties._meta.get_field("description").verbose_name
        self.assertEquals(field_label, "description")

    def test_description_max_length(self):
        properties = Properties.objects.get(id=1)
        max_length = properties._meta.get_field("description").max_length
        self.assertEquals(max_length, )

    def test_price_label(self):
        properties = Properties.objects.get(id=1)
        field_label = properties._meta.get_field("price").verbose_name
        self.assertEquals(field_label, "price")

    def test_location_label(self):
        properties = Properties.objects.get(id=1)
        field_label = properties._meta.get_field("location").verbose_name
        self.assertEquals(field_label, "location")

    def test_location_max_length(self):
        properties = Properties.objects.get(id=1)
        max_length = properties._meta.get_field("location").max_length
        self.assertEquals(max_length, 100)

    def test_street_address_label(self):
        properties = Properties.objects.get(id=1)
        field_label = properties._meta.get_field("street_address").verbose_name
        self.assertEquals(field_label, "street address")

    def test_street_address_max_length(self):
        properties = Properties.objects.get(id=1)
        max_length = properties._meta.get_field("street_address").max_length
        self.assertEquals(max_length, 100)


