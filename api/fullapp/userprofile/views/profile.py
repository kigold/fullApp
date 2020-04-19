from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, mixins, generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from ..serializers import ProfileSerializer
from ..models import Profile, User
from . import CustomJsonRender


class ProfileViewSet(viewsets.ModelViewSet):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    renderer_classes = (CustomJsonRender,)


    @action(methods=['post'], detail=False)
    def login(self, request):
        print(request.data)
        user = User.objects.get(email=request.data['email'])
        print(user)
        token = Token.objects.get_or_create(user=user)
        print("```````````Printing TOken ````````````````")
        print(token[0])
        print(type(token))
        return Response({"token": str(token[0])})
