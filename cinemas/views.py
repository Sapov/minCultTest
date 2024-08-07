from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CinemaGeneralSerializer
from cinemas.models import CinemaGeneral


class CinemasListView(ListAPIView):
    queryset = CinemaGeneral.objects.all()
    serializer_class = CinemaGeneralSerializer


class CinemasDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = CinemaGeneral.objects.all()
    serializer_class = CinemaGeneralSerializer


class CinemasDetail(RetrieveAPIView):
    queryset = CinemaGeneral.objects.all()
    serializer_class = CinemaGeneralSerializer


# def search_by_name(name: str):
#     queryset = CinemaGeneral.objects.filter(name__contains == name)


class CinemasSearchName(APIView):
    def get(self, request):
        lst = CinemaGeneral.objects.all().values()
        return Response({'post': lst})

    def post(self, request, name__contains=None):
        name = request.data['name']
        lst = CinemaGeneral.objects.filter(name__icontains=name).values()
        return Response({'post': lst})


class CinemasSearchAddress(APIView):

    def post(self, request, name__contains=None):
        address = request.data['address']
        lst = CinemaGeneral.objects.filter(full_address__icontains=address).values()
        return Response({'post': lst})
