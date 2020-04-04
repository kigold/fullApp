from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Team


class TeamTest(APITestCase):
    def setUp(self):
        Team.objects.create(name="Eyimba", country="Nigeria")
        Team.objects.create(name="PSG", country="France")

    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Chelsea', 'country': 'England'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 3, "The Number of created team")
        self.assertEqual(Team.objects.latest('pk').name, 'Chelsea')

    def test_edit_team(self):
        url = reverse('team-detail', args=[2])
        data = {'name': 'Monaco', 'country': 'France'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         "Status Code")
        self.assertEqual(Team.objects.get(pk=2).name, 'Monaco',
                         "Edited Team Name")

    def test_get_team(self):
        url = reverse('team-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'][0]['name'], "Eyimba")

    def test_delete_team(self):
        url = reverse('team-detail', args=[2])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         "Status Code")                         
        self.assertFalse(Team.objects.first().name == "Monaco",
                         "Team Name")       
        self.assertEqual(Team.objects.all().count(), 1,
                         "Number of Teams after deleting")
