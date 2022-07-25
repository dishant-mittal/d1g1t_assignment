from django.shortcuts import render

# Create your views here.
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


# @api_view(['GET'])
# def get_avg_happ(request):
#     """
#     Get Happiness Stats for this employee's team
#     """
#     emp_list = Employee.objects.filter(user=request.user)
#     serializer = AuthEmpHappinessTeamStatsSerializer(emp_list, many=True)
#
#     return Response(serializer.data)