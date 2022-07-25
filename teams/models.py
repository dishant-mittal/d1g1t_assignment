from django.db import models

# Create your models here.
class Team(models.Model):
    '''
    This class defines the team name
    '''
    name = models.CharField(unique=True, max_length=200, blank=False)

    def __str__(self):
        return self.name