from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from ..models import Profile, Team
from ..serializers import ProfileSerializer


class ProfileTest(APITestCase):
    def setUp(self):
        Team.objects.create(name="Eyimba", country="Nigeria")
        p1 = ProfileSerializer(
            data={'nick_name': 'admin', 'points': 1000, 'fav_team_id': 1,
                  'user': {'username': 'naruto', 'email': 'admin@yahoo.com',
                           'is_staff': False, 'first_name': 'admin',
                           'last_name': 'badoo',
                           'is_active': True, 'password': 'P@ssw0rd'}})
        p2 = ProfileSerializer(
            data={'nick_name': 'kaycee', 'points': 23, 'fav_team_id': 1,
                  'user': {'username': 'naruto', 'email': 'naruto@konoha.com',
                           'is_staff': False, 'first_name': 'naruto',
                           'last_name': 'uzumaki',
                           'is_active': True, 'password': 'P@ssw0rd'}})
        p1.is_valid()
        p1.save()
        p2.is_valid()
        p2.save()

    def test_create_user(self):
        url = reverse('profile-list')
        data = {'fav_team_id': 1, 'nick_name': 'naruto bae', 'points': 23,
                'user': {'username': 'hinata', 'email': 'hinata@konoha.com',
                         'is_staff': False, 'first_name': 'hinata',
                         'last_name': 'hugo',
                         'is_active': True, 'password': 'P@ssw0rd'}}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Profile.objects.count(), 3,
                         "The Number of created profile")
        self.assertEqual(Profile.objects.latest('pk').user.email,
                         'hinata@konoha.com')
        self.assertEqual(Profile.objects.latest('pk').nick_name,
                         'naruto bae')
        self.assertEqual(Profile.objects.latest('pk').user.first_name,
                         'hinata')

    def test_edit_profile(self):
        url = reverse('profile-detail', args=[2])
        data = {'fav_team_id': 1, 'nick_name': 'chan', 'points': 70,
                'user': {'username': 'sakura', 'email': 'sakura@konoha.com',
                         'is_staff': False, 'first_name': 'sakura',
                         'last_name': 'chan',
                         'is_active': True, 'password': 'P@ssw0rd'}}
        response = self.client.put(url, data, format='json')

        self.assertEqual(Profile.objects.get(pk=2).nick_name, 'chan',
                         "Edited Nick Name")
        self.assertEqual(response.status_code, status.HTTP_200_OK,
                         "Status Code")
        self.assertEqual(Profile.objects.get(pk=2).user.email,
                         'sakura@konoha.com', "Edited Email")
        self.assertEqual(Profile.objects.get(pk=2).points, 70,
                         "Edited Points")

    def test_get_profile(self):
        url = reverse('profile-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 2)
        self.assertEqual(response.data['results'][0]['nick_name'], "admin")
        self.assertEqual(response.data['results'][0]['user']['email'],
                         "admin@yahoo.com")
        self.assertEqual(response.data['results'][1]['nick_name'], "kaycee")
        self.assertEqual(response.data['results'][1]['user']['email'],
                         "naruto@konoha.com")
        self.assertEqual(response.data['results'][1]['user']['first_name'],
                         "naruto")

    def test_delete_profile(self):
        url = reverse('profile-detail', args=[1])
        response = self.client.delete(url, format='json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT,
                         "Status Code")
        self.assertFalse(Profile.objects.first().user.first_name == "admin",
                         "Profile Name")
        self.assertEqual(Profile.objects.all().count(), 1,
                         "Number of Profiles after deleting")
