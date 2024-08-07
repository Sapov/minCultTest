from rest_framework import serializers
from cinemas.models import CinemaGeneral


class CinemaGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaGeneral
        fields = '__all__'
