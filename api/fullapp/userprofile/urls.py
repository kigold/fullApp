from django.urls import include, path
from django.conf.urls import url
from .views import TeamList, TeamDetails, TeamViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')

'''urlpatterns = [
    path("teams/", TeamList.as_view(), name="teams_list"),
    path("teams/<int:pk>/", TeamDetails.as_view(), name="teams_details"),
    path("team/", include(router.urls))
]'''

# urlpatterns = router.urls
urlpatterns = [url(r'^', include(router.urls)),
               path("teams/deleterange/<int:pk>",
               TeamViewSet.as_view({"post": "deleterange"}))
               ]
