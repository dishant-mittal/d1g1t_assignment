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


@api_view(['GET'])
def get_avg_happ(request):
    """
    Get Happiness Stats for this employee's team
    """
    if not request.user.is_authenticated: #### return avg across all the teams

        return redirect(reverse_lazy('login'))
    else: ### return all happiness levels inserted across any team

        happs = Happiness.objects.all()
        serializer = HappinessSerializer(happs, many=True)

    return Response(serializer.data)



@api_view(['POST'])
def add_todays_happ(request):
    """
    Add Happiness Level for today (Only accepts the request from loggedin user)
    """

    emp = Employee.objects.filter(user=request.user).first() ### Each emp is associated to a particular user
    if not emp: raise ValidationError("Invalid Request..Please Register this user as an employee from Django Admin first")

    #### If an authenticated user as already posted today's happinees then further posting not allowed
    happiness_queryset = Happiness.objects.filter(emp=emp, created_at=datetime.now().date())
    if happiness_queryset.exists():
        raise ValidationError("Invalid Request..You have already Posted your Happiness Level for today. Please come back tomorrow to enter!")

    serializer = HappinessSerializer(data=request.data)
    if serializer.is_valid():
        # serializer.save()
        serializer.save(emp=emp)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)