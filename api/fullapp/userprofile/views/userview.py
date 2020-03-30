from django.contrib.auth.models import Group
from rest_framework import viewsets
# from fullapp.userprofile.serializers import UserSerializer, GroupSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    pass


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    pass
