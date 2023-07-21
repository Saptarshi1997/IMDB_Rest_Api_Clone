from imdb_drf_app.models import *
from imdb_drf_app.serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import mixins, generics

# Create your views here.

class StreamPlatformListAV(APIView):

    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class SingleStreamPlatformAV(APIView):

    def get(self, request, pk):
        platform = StreamPlatform.objects.get(pk = pk)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk = pk)
        serializer = StreamPlatformSerializer(platform, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk = pk)
        platform.delete()
        return Response({"message": "The particular platform has been deleted!!!"})


class WatchListAV(APIView):

    def get(self, request):
        watchlist = Watch.objects.all()
        serializer = WatchSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = WatchSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        

class SingleWatchAV(APIView):

    def get(self, request, pk):
        watch = Watch.objects.get(pk = pk)
        serializer = WatchSerializer(watch)
        return Response(serializer.data)
    
    def put(self, request, pk):
        watch = Watch.objects.get(pk = pk)
        serializer = WatchSerializer(watch, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, pk):
        watch = StreamPlatform.objects.get(pk = pk)
        watch.delete()
        return Response({"message": "The particular watch has been deleted!!!"})
    

class ReviewListAV(generics.ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watch=pk)
    
class ReviewCreateAV(generics.CreateAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watch = Watch.objects.get(pk=pk)
        serializer.save(watch=watch)
    

class SingleReviewAV(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer