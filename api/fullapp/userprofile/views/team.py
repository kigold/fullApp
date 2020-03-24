from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, mixins, generics
from rest_framework import viewsets
from rest_framework.decorators import action
from ..serializers import TeamSerializer
from ..models import Team
from ..service import TeamService


'''class TeamList(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class TeamDetails(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)'''


class TeamList(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    # queryset = Team.objects.all()
    # serializer_class = TeamSerializer

    @action(methods=['get'], detail=True, url_path="gigi")
    def get(self, request, *args, **kwargs):
        query = Team.objects.all()
        serializer_class = TeamSerializer(query, many=True)
        return Response(serializer_class.data)

    '''@action(methods=['post'], detail=False)
    def post(self, request):
        return self.create(request, *args, **kwargs)'''


class TeamDetails(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]
    # queryset = Team.objects.all()
    # serializer_class = TeamSerializer

    @action(methods=['get'], detail=True)
    def getted(self, request, pk):
        queryset = get_object_or_404(Team, pk=pk)
        data = TeamSerializer(queryset).data
        return Response(data)


class TeamViewSet(viewsets.ModelViewSet):

    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    _team_service = TeamService()

    @action(methods=['get'], detail=False)
    def custom_method(self, request):
        query = TeamService.custom_method()
        serializer_class = TeamSerializer(query, many=True)
        return Response(serializer_class.data)

    @action(methods=['post'], detail=False)
    def custom_method_two(self, request):
        query = self._team_service.custom_method_two(request.data)
        # serializer_class = TeamSerializer(query, many=False)
        if query['has_error']:
            return Response({'error': query['errors']})
        result = TeamSerializer(query['result'])
        return Response(result.data)

    @action(methods=['post'], detail=False)
    def deleterange(self, request, pk):
        print(pk)
        query = self._team_service.delete_range(pk)
        if query['has_error']:
            return Response({'error': query['errors']})
        return Response("Successfully deleted items")
