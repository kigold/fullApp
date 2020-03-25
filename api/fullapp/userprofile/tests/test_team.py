from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Team


class TeamTest(APITestCase):
    def test_createTeam(self):
        url = reverse('team-list')
        print(')))))))))))))))))URL(((((((((((((((((')
        print(url)
        data = {'Name': 'Chelsea', 'Country': 'England'}
        response = self.client.post(url, data, format='json')
        print(')))))))))))))))))RESPONSE(((((((((((((((((')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Team.objects.get().name, 'Chelsea')

    def test_getTeam(self):
        url = reverse('team-list')
        print(')))))))))))))))))URL(((((((((((((((((')
        print(url)
        response = self.client.get(url)
        print(')))))))))))))))))RESPONSE(((((((((((((((((')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Team.objects.count(), 0)
