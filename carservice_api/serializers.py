# from rest_framework import serializers
# from carservice_api import models

# class MaintenanceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Maintenance
#         fields = ('id', 'car_id', 'type', 'created_at')
#         extra_kwargs = {'car_Id': {'required': True}}
    
#     def create(self, validated_data):
#         maintenance = models.Maintenance.objects.create(**validated_data)

#         return maintenance

# class CarsSerializer(serializers.ModelSerializer):
#     maintenance = MaintenanceSerializer(many=True, read_only=True)

#     class Meta:
#         model = models.Car
#         fields = ('id', 'vin', 'brand', 'model', 'fuel', 'power', 'horse_power', 'plate', 'maintenance')
#         extra_kwargs = {'maintenance': {'required': False}}
    
#     def create(self, validated_data):
#         car = models.Car.objects.create(**validated_data)

#         return car