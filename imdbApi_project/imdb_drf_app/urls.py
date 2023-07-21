from django.urls import path
from imdb_drf_app.views import *

urlpatterns = [
    path('watch/list', WatchListAV.as_view(), name='watch_list'),
    path('watch/<int:pk>', SingleWatchAV.as_view(), name='single_watch'),
    path('platform/list', StreamPlatformListAV.as_view(), name='stream_platform'),
    path('platform/<int:pk>', SingleStreamPlatformAV.as_view(), name='single_platform'),
    # path('review/list', ReviewListAV.as_view(), name='review_list'),
    # path('review/<int:pk>', SingleReviewAV.as_view(), name='single_review'),
    path('platform/<int:pk>/review', ReviewListAV.as_view(), name='review_list'),
    path('platform/<int:pk>/post-review', ReviewCreateAV.as_view(), name='review_list'),
    path('platform/review/<int:pk>', SingleReviewAV.as_view(), name='single_review'),
]
