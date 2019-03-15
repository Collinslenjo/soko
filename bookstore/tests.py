from .models import *
from .serializers import *
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
		user = User.objects.get_or_create(username="test_user")
		self.client.force_authenticate(user=user)
		self.get_user_profile(user[0])
		self.user_id = user[0].id
		category_test = {"name":"fiction", "charge":1}
		category_response = self.client.post('/api/categories/',category_test)
		self.category_id = category_response.data


class getCategoriesTest(BaseViewTest):
	def get_categories_test(self):
		response = self.client.get(reverse('categories'))
		expected = BookCategory.objects.all()
		serialized = BookCategorySerializer(expected,many=True)
		self.assertEqual(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_category(self):
		category = {"name":"fiction", "charge":1}
		response = self.client.post('/api/categories/',category)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class getBooksTest(BaseViewTest):
	def get_books_test(self):
		response = self.client.get(reverse('books'))
		expected = Book.objects.all()
		serialized = BookSerializer(expected,many=True)
		self.assertEqual(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_book(self):
		book = {"bookname":"A Song of Ice and Fire", "category":self.category_id['id'],"user":self.user_id}
		response = self.client.post('/api/books/',book)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class getRentedBooksTest(BaseViewTest):
	def get_books_test(self):
		response = self.client.get(reverse('rentbooks'))
		expected = RentedBook.objects.all()
		serialized = RentedBookCategorySerializer(expected,many=True)
		self.assertEqual(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_book(self):
		book = {"bookname":"A Dance of Dragons", "category":self.category_id['id'],"user":self.user_id}
		book_response = self.client.post('/api/books/',book)
		rentbook = {"book":book_response.data['id'],"user":self.user_id}
		response = self.client.post('/api/rentbooks/',rentbook)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)