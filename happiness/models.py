from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
from employees.models import *

class Happiness(models.Model):
    '''
    This class defines the happiness of an employee on a particular date
    '''
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=False,
                              related_name='happiness_level')

    # Assuming that the happiness level can only range from 1 - 10
    level = models.PositiveIntegerField(blank=False,null=False,validators=[MaxValueValidator(10),MinValueValidator(1)])

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Happiness Level of '+self.emp.user.username + ' on '+ str(self.created_at).split(' ')[0] +' was: '+str(self.level)

