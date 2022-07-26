from rest_framework.test import APITestCase
from happiness.models import *
from django.contrib.auth.models import User
from django.test import Client

class TeamsAPITestCase(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='dishant')
        user.set_password('dishant')
        user.save()

        c = Client()
        c.login(username='dishant', password='dishant')
        # print("user_id is", c.session['_auth_user_id'])
        Team.objects.create(name='devops')
        Employee.objects.create(user_id=1, team_id=1)  ### employee created
        Happiness.objects.create(emp_id=1,level=8)

    def test_team_create_success(self):
        # qs = User.objects.filter(username='dishant')
        qs = Team.objects.filter(name='devops')
        # print("team id is", qs.id)
        self.assertEquals(qs.count(), 1)

    def test_get_method(self):
        url = 'http://127.0.0.1:8080/teams/get-happiness/'
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.data,{'avg_happiness': 8.0})
