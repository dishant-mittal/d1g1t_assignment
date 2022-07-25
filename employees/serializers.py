"""""""""""""""""""""""""""""""""""""""""""""""""""
Intro
""""""""""""""""""""""""""""""""""""""""""""""""""""""
Author: Dishant Mittal
Version: 1.0
Email: dishantmittal31@gmail.com
Date Created: 2022-07-25
"""""""""""""""""""""""""""""""""""""""""""""""""""

# from rest_framework import serializers
# from django.db.models import Avg, Max, Min, Sum
# from .models import *
# from happiness.models import *
#
#
#
# class AuthEmpHappinessTeamStatsSerializer(serializers.ModelSerializer):
#     '''
#     Class for serializing and deserialing the data queried/ stored
#     '''
#     # team = serializers.StringRelatedField(read_only=True)
#     # avg_happiness = serializers.SerializerMethodField()
#
#     # id = serializers.IntegerField(read_only=True)
#     # level = serializers.IntegerField(required=True)
#     # created_at = serializers.DateTimeField(read_only=True)
#
#     class Meta:
#         model = Employee
#         fields = ["likes_count"]
#
#     # def get_avg_happiness(self, obj):
#     #     avg = Happiness.objects.filter(emp=self).aggregate(avg_happiness=Avg('level'))
#     #     # avg = Team.objects.all().aggregate(avg_happiness=Avg('level'))
#     #     return avg["avg_happiness"]