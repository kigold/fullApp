from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from .views import *
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'profile', ProfileViewSet, basename='profile')
router.register(r'games', GameViewSet, basename='game')
router.register(r'cup', CupViewSet, basename='cup')
router.register(r'cupgames', CupGameViewSet, basename='cupgame')
router.register(r'league', LeagueViewSet, basename='league')
router.register(r'leaguegames', LeagueGameViewSet, basename='leaguegame')
router.register(r'challenge', ChallengeViewSet, basename='challenge')

'''urlpatterns = [
    path("teams/", TeamList.as_view(), name="teams_list"),
    path("teams/<int:pk>/", TeamDetails.as_view(), name="teams_details"),
    path("team/", include(router.urls))
]'''

# urlpatterns = router.urls
urlpatterns = [url(r'^', include(router.urls)),
               url(r'^api-token-auth/', CustomAuthToken.as_view()),
               path("auth/login",
                    ProfileViewSet.as_view({"post": "login"})),
               path("teams/deleterange/<int:pk>",
                    TeamViewSet.as_view({"post": "deleterange"})),
               path("games/fixtures/<int:pk>",
                    GameViewSet.as_view({"put": "updatefixtures"})),
               path("games/fixture/<int:pk>",
                    GameViewSet.as_view({"get": "get_fixture"})),
               ]


#url(r'^articles/(?P\d{2})/(?P\d{4})', 'viewArticles', name = 'articles'