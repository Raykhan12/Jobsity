from django.test import TestCase
from rest_framework import status

class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('/stock')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_index_fail(self):
        """The index page loads properly"""
        response = self.client.get('/fake')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)