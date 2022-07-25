from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Max, Min, Sum
from teams.models import *
# from happiness.models import Happiness

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='associated_emp')

    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=False, blank=False,
                              related_name='associated_team')  #####The reason for adding related name is because of the reasons mentioned in reverse_name_clash directory

    def __str__(self):
        return self.user.username

    # def likes_count(self):
    #     avg = Happiness.objects.filter(emp=self).aggregate(Avg('level'))
    #     return avg

    # def likes_count(self):
    #     return self.likes.all().count()