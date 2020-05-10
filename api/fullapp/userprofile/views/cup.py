from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework import (authentication, generics, mixins, permissions,
                            viewsets)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Cup
from ..serializers import CupSerializer

# from . import CustomJsonRender


class CupViewSet(viewsets.ModelViewSet):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Cup.objects.all()
    serializer_class = CupSerializer
    # renderer_classes = (CustomJsonRender,)
