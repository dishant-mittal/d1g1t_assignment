"""""""""""""""""""""""""""""""""""""""""""""""""""
Intro
""""""""""""""""""""""""""""""""""""""""""""""""""""""
Author: Dishant Mittal
Version: 1.0
Email: dishantmittal31@gmail.com
Date Created: 2022-07-25
"""""""""""""""""""""""""""""""""""""""""""""""""""
from rest_framework import serializers
from django.db.models import Avg, Max, Min, Sum
from django.db.models import Count
from .models import *
from happiness.models import *

class AuthEmpTeamHappinessStatsSerializer(serializers.ModelSerializer):
    '''
    Class for serializing and deserialing the data queried/ stored
    '''
    team = serializers.StringRelatedField(read_only=True)
    avg_happiness = serializers.SerializerMethodField()
    emp_count_by_level = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = "__all__"

    def get_avg_happiness(self, obj):
        emps = Employee.objects.filter(team_id=obj.id).values_list('id', flat=True)
        happs = Happiness.objects.filter(emp__in=emps)
        avg = happs.aggregate(avg_happiness=Avg('level'))
        return avg["avg_happiness"]

    def get_emp_count_by_level(self,obj):
        emps = Employee.objects.filter(team_id=obj.id).values_list('id', flat=True)
        happs = Happiness.objects.filter(emp__in=emps)
        qs = happs.values('level').annotate(Count('emp_id', distinct=True))
        return qs


