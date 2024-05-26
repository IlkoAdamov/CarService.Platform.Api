from rest_framework import serializers
from carservice_api import models

class ServiceSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Service
        fields = ('id', 'maintenance_id', 'service_type', 'title', 'description')
        extra_kwargs = {'maintenance_id': {'required': True}}

    def create(self, validated_data):
        service = models.Service.objects.create(**validated_data)
        return service