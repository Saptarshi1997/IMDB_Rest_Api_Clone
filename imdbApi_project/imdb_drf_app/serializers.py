from rest_framework import serializers
from imdb_drf_app.models import *


class WatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watch
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

    # watchlist = WatchSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"