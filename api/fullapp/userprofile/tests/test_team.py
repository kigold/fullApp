from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Team


class TeamTest(APITestCase):
    def setUp(self):
        Team.objects.create(name="Eyimba", country="Nigeria")
        Team.objects.create(name="PSG", country="France")

    def test_createTeam(self):
        url = reverse('team-list')
        data = {'name': 'Chelsea', 'country': 'England'}
        response = self.client.post(url, data, format='json')

        print(')))))))))))))))))RESPONSE(((((((((((((((((')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 3, "The Number of created team")
        self.assertEqual(Team.objects.latest('pk').name, 'Chelsea')

    def test_getTeam(self):
        url = reverse('team-list')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("COunt teams")
        print(response.data)
        print(response.data['results'])
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'][0]['name'], "Eyimba")
        
