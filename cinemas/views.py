from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .serializers import CinemaGeneralSerializer
from cinemas.models import CinemaGeneral


class CinemasViewSet(ModelViewSet):
    queryset = CinemaGeneral.objects.all()
    serializer_class = CinemaGeneralSerializer

    @action(methods=['post'], detail=False)
    def search_address(self, request):
        """поиск по адресу
        {"address":"Воронеж"}"""
        address = request.data['address']
        lst = CinemaGeneral.objects.filter(full_address__icontains=address).values()
        return Response({'post': lst})

    @action(methods=['post'], detail=False)
    def search_name(self, request):
        """поиск по имени кинотеатра
            {"name":"Космос"}"""
        address = request.data['address']
        lst = CinemaGeneral.objects.filter(full_address__icontains=address).values()
        return Response({'post': lst})



# class CinemasSearchName(APIView):
#
#     def post(self, request):
#         serializer = CinemaGeneralSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         if request.data['name']:
#             name = request.data['name']
#             lst = CinemaGeneral.objects.filter(name__icontains=name)
#             res = CinemaGeneralSerializer(lst, many=True).data
#             return Response({'post': res})
#
#
# class CinemasSearchAddress(APIView):
#
#     def post(self, request, name__contains=None):
#         address = request.data['address']
#         lst = CinemaGeneral.objects.filter(full_address__icontains=address).values()
#         return Response({'post': lst})
