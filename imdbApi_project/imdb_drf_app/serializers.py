from rest_framework import serializers
from imdb_drf_app.models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        exclude = ('watch',)
        # fields = "__all__"

class WatchSerializer(serializers.ModelSerializer):
    # review = serializers.StringRelatedField(many=True, read_only=True)
    review = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Watch
        fields = "__all__"


class StreamPlatformSerializer(serializers.ModelSerializer):

    # watchlist = WatchSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = StreamPlatform
        fields = "__all__"