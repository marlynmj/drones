from rest_framework import serializers
from api.models import Dron, Drug, Historial, MODELO, WEIGHT_LIMIT, PERCENTAGE_VALIDATOR, STATUS, alphanumeric, alphanumericCode


# class DronSerializer(serializers.Serializer):
#     serialNumber = serializers.CharField(max_length=150)
#     model = serializers.CharField(choices=MODELO, default=0, max_length=2)
#     weightLimit = serializers.DecimalField(max_digits=3, decimal_places=0, default=0, validators=WEIGHT_LIMIT)
#     batteryCapacity = serializers.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)
#     status = serializers.CharField(choices=STATUS, default=0, max_length=3)
    
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Dron.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.serialNumber = validated_data.get('serialNumber', instance.title)
#         instance.model = validated_data.get('model', instance.model)
#         instance.weightLimit = validated_data.get('weightLimit', instance.weightLimit)
#         instance.batteryCapacity = validated_data.get('batteryCapacity', instance.batteryCapacity)
#         instance.status = validated_data.get('status', instance.status)
#         instance.save()
#         return instance
        
class DronSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dron
        fields = '__all__'

class DrugSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drug
        # fields = ['id', 'name', 'weight', 'code', 'image']
        fields = '__all__'
        
class HistorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Historial
        # fields = ['id', 'name', 'weight', 'code', 'image']
        fields = '__all__'