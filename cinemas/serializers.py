from rest_framework import serializers
from cinemas.models import CinemaGeneral


class CinemaGeneralSerializer(serializers.ModelSerializer):
    class Meta:
        model = CinemaGeneral
        fields = '__all__'


# class CinemaGeneralSerializer(serializers.Serializer):
#         id_service = serializers.IntegerField(read_only=True)
#         name = serializers.CharField(read_only=True)
#         description = serializers.CharField(read_only=True)
#         street = serializers.CharField(read_only=True)
#         comment = serializers.CharField(read_only=True)
#         full_address = serializers.CharField(read_only=True)
#         type = serializers.CharField(read_only=True)
#         category = serializers.CharField(read_only=True)
#         category_sysName = serializers.CharField(read_only=True)
#         website = serializers.CharField(read_only=True)
#         email = serializers.CharField(read_only=True)
#         phones = serializers.CharField(read_only=True)
