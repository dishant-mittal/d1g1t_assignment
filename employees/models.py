from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min, Sum
from teams.models import *
# from happiness.models import Happiness

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='associated_emp')

    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, blank=False,
                              related_name='associated_team')

    def __str__(self):
        return self.user.username