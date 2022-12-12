from django.shortcuts import render
from .models import Song
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import SongSerializer

# Create your views here.

class SongListView(ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer