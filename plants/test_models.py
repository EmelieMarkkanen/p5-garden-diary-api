from django.test import TestCase
from django.contrib.auth.models import User
from datetime import date
from .models import Plants


class PlantsModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(
            username='testuser',
            password='testpass')
        Plants.objects.create(
            owner=user,
            name='Rose',
            plant_type='shrub',
            planted_at=date.today(),
            care_instructions='Water regularly'
        )

    def test_name_max_length(self):
        plant = Plants.objects.get(id=1)
        max_length = plant._meta.get_field('name').max_length
        self.assertEquals(max_length, 255)

    def test_ordering(self):
        plants = Plants.objects.all()
        expected_ordering = ['-created_at']
        self.assertListEqual(plants.model._meta.ordering, expected_ordering)

    def test_string_representation(self):
        plant = Plants.objects.get(id=1)
        self.assertEqual(str(plant), '1 Rose')
