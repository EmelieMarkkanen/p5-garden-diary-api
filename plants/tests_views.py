from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Plants


class PlantsListViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
                username='testuser',
                password='testpassword')
        self.client.force_authenticate(user=self.user)

    def test_plants_list(self):
        response = self.client.get('/plants/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_plant(self):
        data = {'name': 'Rose', 'care_instructions': 'Some instructions'}
        response = self.client.post('/plants/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class PlantsDetailedViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword')
        self.plant = Plants.objects.create(
            name='Rose',
            care_instructions='Some instructions',
            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_retrieve_plant(self):
        response = self.client.get(f'/plants/{self.plant.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_plant(self):
        data = {
            'name': 'Sunflower',
            'care_instructions': 'Some other instructions'}
        response = self.client.put(f'/plants/{self.plant.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_plant(self):
        response = self.client.delete(f'/plants/{self.plant.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
