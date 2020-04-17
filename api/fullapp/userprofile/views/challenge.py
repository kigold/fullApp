from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, mixins, generics
from rest_framework import viewsets
from rest_framework.decorators import action
from ..serializers import ChallengeSerializer
from ..models import Challenge
from . import CustomJsonRender


class ChallengeViewSet(viewsets.ModelViewSet):

    queryset = Challenge.objects.all()
    serializer_class = ChallengeSerializer
    renderer_classes = (CustomJsonRender,)
