from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CinemaGeneralSerializer
from .models import CinemaGeneral


class CinemasListView(ListAPIView):
    queryset = CinemaGeneral.objects.all()
    serializer_class = CinemaGeneralSerializer


class CinemasDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CinemaGeneral.objects.all()
    serializer_class = CinemaGeneralSerializer


class CinemasDetail(RetrieveAPIView):
    queryset = CinemaGeneral.objects.all()
    serializer_class = CinemaGeneralSerializer