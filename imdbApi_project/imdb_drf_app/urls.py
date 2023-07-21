from django.urls import path
from imdb_drf_app.views import *

urlpatterns = [
    path('watch/list', WatchListAV.as_view(), name='watch_list'),
    path('watch/<int:pk>', SingleWatchAV.as_view(), name='single_watch'),
    path('platform/list', StreamPlatformListAV.as_view(), name='stream_platform'),
    path('platform/<int:pk>', SingleStreamPlatformAV.as_view(), name='single_platform'),
    path('review/list', ReveiwListAV.as_view(), name='review_list'),
]
