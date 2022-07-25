from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .models import *
from employees.models import *
from datetime import datetime
from .serializers import *
from rest_framework.exceptions import ValidationError
from employees.models import *
from teams.models import *

# Create your views here.


@api_view(['GET'])
def get_avg_happ(request):
    """
    Get Happiness Stats for this employee's team
    """
    if not request.user.is_authenticated: #### return avg across all the teams
        happs = Happiness.objects.all()
        avg = happs.aggregate(avg_happiness=Avg('level'))
        data = avg
    else: ### return the statistics of user's team
        team_name = Employee.objects.filter(user=request.user).first().team.name
        teams = Team.objects.filter(name=team_name)  ###list will contain only single team name
        serializer = AuthEmpTeamHappinessStatsSerializer(teams, many=True)
        data = serializer.data
    return Response(data = data)