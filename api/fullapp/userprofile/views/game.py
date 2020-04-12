from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView, status
from rest_framework.response import Response
from rest_framework import authentication, permissions, mixins, generics
from rest_framework import viewsets
from rest_framework.decorators import action
from django.db import transaction
from ..serializers import GameSerializer
from ..models import Game, Profile
from . import BasicPagination


class GameViewSet(viewsets.ModelViewSet):

    # queryset = Game.objects.all()
    serializer_class = GameSerializer
    pagination_class = BasicPagination

    @action(methods=['get'], detail=True)
    def get_fixture(self, request, pk):
        queryset = get_object_or_404(Game, pk=pk)
        data = GameSerializer(queryset).data
        return Response(data)

    @action(methods=['get'], url_path='fixtures', detail=False)
    def get(self, request):
        instance = Game.objects.all()
        # .order_by('pk')
        page = self.paginate_queryset(instance)
        if page is not None:
            serializer_class = self.get_paginated_response(
                self.serializer_class(page, many=True).data)
        else:
            serializer_class = self.serializer_class(instance, many=True)
        # data = GameSerializer(queryset, many=True).data
        return Response(serializer_class.data)

    @action(methods=['post'], url_path='fixtures', detail=False)
    def addfixtures(self, request):
        try:
            with transaction.atomic():
                serializer_class = GameSerializer(data=request.data)
                if 'status' in request.data:
                    if request.data['status'] == 2:
                        serializer_class.validate_for_played_game()
                if not serializer_class.is_valid():
                    return Response({'error': serializer_class.errors})
                serializer_class.save()
                # calculate users points if match is played
                if 'status' in request.data:
                    if request.data['status'] == 2:
                        GameViewSet.compute_user_points(
                            request.data['home_user_id'],
                            request.data['away_user_id'],
                            request.data['home_score'],
                            request.data['away_score'])
                return Response(serializer_class.data)
        except Exception as e:
            raise e

    @action(methods=['put'], detail=True)
    def updatefixtures(self, request, pk=None):
        try:
            with transaction.atomic():
                game = get_object_or_404(Game, pk=pk)
                if game.status is 2:
                    return Response({'error': "Game already played," +
                                     " cannot update"},
                                    status=status.HTTP_400_BAD_REQUEST)
                serializer_class = GameSerializer(instance=game,
                                                  data=request.data)
                if 'status' in request.data:
                    if request.data['status'] == 2:
                        serializer_class.validate_for_played_game()
                if not serializer_class.is_valid():
                    return Response({'error': serializer_class.errors})
                serializer_class.save()
                # calculate users points if match is played
                if 'status' in request.data:
                    if request.data['status'] == 2:
                        GameViewSet.compute_user_points(
                            request.data['home_user_id'],
                            request.data['away_user_id'],
                            request.data['home_score'],
                            request.data['away_score'])
                return Response(serializer_class.data)
        except Exception as e:
            raise e

    def compute_user_points(user1_id, user2_id, user1_score,
                            user2_score):
        user1 = Profile.objects.get(pk=user1_id)
        user2 = Profile.objects.get(pk=user2_id)
        if(user1_score < user2_score and user1.points > user2.points):
            user2.points = user2.points + 3
            user1.points = user1.points - 3
            user2.save()
            user1.save()
        if(user2_score < user1_score and user2.points > user1.points):
            user1.points = user1.points + 3
            user2.points = user2.points - 3
            user2.save()
            user1.save()







                
                
