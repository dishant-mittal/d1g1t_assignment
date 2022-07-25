from rest_framework import serializers
from django.db.models import Avg, Max, Min, Sum
from .models import *
#
class HappinessSerializer(serializers.ModelSerializer):
    '''
    Class for serializing and deserialing the data queried/ stored
    '''
    happ_emp = serializers.StringRelatedField(read_only=True)
    # id = serializers.IntegerField(read_only=True)
    # level = serializers.IntegerField(required=True)
    # created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Happiness
        fields = "__all__"

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Happiness` instance, given the validated data.
    #     """
    #     return Happiness.objects.create(**validated_data)



