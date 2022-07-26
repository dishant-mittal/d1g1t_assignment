from rest_framework.test import APITestCase
from happiness.models import *
from django.contrib.auth.models import User
from django.test import Client

class EmployeeAPITestCase(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='dishant')
        user.set_password('dishant')
        user.save()

        c = Client()
        c.login(username='dishant', password='dishant')
        # print("user_id is", c.session['_auth_user_id'])
        Team.objects.create(name='devops')
        Employee.objects.create(user_id=1, team_id=1) ### employee created

    def test_employee_create_success(self):
        qs = Employee.objects.filter(user_id=1)
        # qs = Team.objects.filter(name='devops')
        # print("team id is", qs.id)
        self.assertEquals(qs.count(), 1)