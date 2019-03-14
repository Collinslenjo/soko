from django.urls import reverse
from django.test import TestCase
from rest_framework.views import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient

# Create your tests here.
class BaseViewTest(APITestCase):
	# test authentication
	def test_authentication(self):
		client_ = APIClient()
		response = client_.get(reverse("index"))
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	@staticmethod
	def get_user_profile(user=None):
		if user != None:
			User.objects.get(username=user)

	def setUp(self):
		client = APIClient()
		user = User.objects.get_or_create(username="collins")
		self.client.force_authenticate(user=user)
		self.get_user_profile(user[0])