from rest_framework import serializers
from django.db.models import Avg, Max, Min, Sum
from .models import *
#
class HappinessSerializer(serializers.ModelSerializer):
    '''
    Class for serializing and deserialing the data queried/ stored
    '''
    happ_emp = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Happiness
        fields = "__all__"


