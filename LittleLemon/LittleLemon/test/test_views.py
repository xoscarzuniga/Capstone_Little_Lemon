from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import menuSerializer  # Asegúrate de usar el nombre exacto de tu serializador (MenuSerializer o menuSerializer)

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
        Menu.objects.create(title="Pizza", price=120, inventory=50)

    def test_getall(self):
        items = Menu.objects.all()
        serialized_data = menuSerializer(items, many=True).data
        response = self.client.get('/api/menu-items/')  # 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serialized_data)