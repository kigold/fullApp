from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'games', GameViewSet, basename='game')
router.register(r'cup', CupViewSet, basename='cup')
router.register(r'cupgames', CupGameViewSet, basename='cupgame')

'''urlpatterns = [
    path("teams/", TeamList.as_view(), name="teams_list"),
    path("teams/<int:pk>/", TeamDetails.as_view(), name="teams_details"),
    path("team/", include(router.urls))
]'''

# urlpatterns = router.urls
urlpatterns = [url(r'^', include(router.urls)),
               path("teams/deleterange/<int:pk>",
                    TeamViewSet.as_view({"post": "deleterange"})),
               path("games/fixtures/<int:pk>",
                    GameViewSet.as_view({"put": "updatefixtures"})),
               path("games/fixture/<int:pk>",
                    GameViewSet.as_view({"get": "get_fixture"})),
               ]


#url(r'^articles/(?P\d{2})/(?P\d{4})', 'viewArticles', name = 'articles'