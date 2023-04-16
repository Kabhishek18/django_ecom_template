from django.test import TestCase
from django.urls import reverse
from .views import index
from .models import Products, Categories


class IndexViewTestCase(TestCase):
    def setUp(self):
        self.categories = Categories.objects.all()
        self.products = Products.objects.all()

    def test_index_view(self):
        url = reverse('home')
            response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'v1/index.html')
        self.assertEqual(len(response.context['categories']), len(self.categories))
        self.assertEqual(len(response.context['products']), len(self.products))
