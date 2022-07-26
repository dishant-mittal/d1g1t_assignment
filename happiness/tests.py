from rest_framework.test import APITestCase
from happiness.models import *
from django.contrib.auth.models import User
from django.test import Client

class HappinessAPITestCase(APITestCase):
    def setUp(self) -> None:
        user = User.objects.create(username='dishant')
        user.set_password('dishant')
        user.save()

        c = Client()
        c.login(username='dishant', password='dishant')
        # print("user_id is", c.session['_auth_user_id'])
        Team.objects.create(name='devops')
        Employee.objects.create(user_id=1, team_id=1) ### employee created
        # Happiness.objects.create(emp_id=1,level=8)

    def test_post_method_success(self):
        url = "http://127.0.0.1:8080/happiness/post-happiness/"
        data = {
            'level': 9,
            'emp_id': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 201)



    def test_post_method_fail(self):
        url = "http://127.0.0.1:8080/happiness/post-happiness/"
        data = {
            'level': 12, ### should fail bcz level is capped at 10
            'emp_id': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, 400)


