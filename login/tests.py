from django.test import TestCase, Client
from .models import Task
from .views import welcome
from django.contrib.auth.models import User
from django.urls import reverse


class TaskTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("alex", password="240202e")
        self.task = Task.objects.create(
            title="comer", content="arroz", user=self.user
        )

    def test_user_task(self):
        task = self.task
        self.assertEqual(task.user.username, "alex")
        self.assertEqual(task.title,"comer")
        
        


class WelcomeTestCase(TestCase):
    def setUp(self):
        self.client == Client()

    def test_view(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        response == self.client.get("sign/")
        self.assertEqual(response.status_code,200)
    def test_template(self):
        response= self.client.get("")
        self.assertTemplateUsed(response,"welcome.html")