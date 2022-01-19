from cgi import print_form
from urllib import request
from urllib.request import Request
from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User, CustomAccountManager
from accounts.backends import MyAuthBackend
from django.contrib.auth import  login, logout

from courses.models import Course


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_login = reverse('login')
        self.user_register = reverse('register')
        self.user_dashboard = reverse('dashboard')
        self.enroll_the_course = reverse('enroll_the_course')

    def test_user_login_GET(self):
        response = self.client.get(self.user_login)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    
    def test_user_register_GET(self):
        response = self.client.get(self.user_register)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    