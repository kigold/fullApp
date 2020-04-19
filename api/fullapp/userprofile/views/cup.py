from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, mixins, generics
from rest_framework import viewsets
from rest_framework.decorators import action
from ..serializers import CupSerializer
from ..models import Cup
# from . import CustomJsonRender


class CupViewSet(viewsets.ModelViewSet):

    queryset = Cup.objects.all()
    serializer_class = CupSerializer
    # renderer_classes = (CustomJsonRender,)
