from .models import *
from .serializers import *
from datetime import datetime
from .permissions import IsOwner
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import status
from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

# Create your views here.
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
def index(req):
	rentedBooks = RentedBook.objects.filter(user=req.user.id)
	rented =[]

	for mybooks in rentedBooks:
		charges = 1
		if mybooks.dateReturned is not None:
			days_calc = mybooks.dateReturned.date() - mybooks.dateBorrowed.date()
			days = days_calc.days
		else:
			days_calc = datetime.now().date() - mybooks.dateBorrowed.date()
			days = days_calc.days
		cost_per_book = days * charges
		rented.append(cost_per_book)

	result = sum(rented)
	return HttpResponse("Your cost is KES."+str(result))


@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
class ListCategories(generics.ListCreateAPIView):
	queryset = BookCategory.objects.all()
	serializer_class = BookCategorySerializer

	def post(self,request, **kwargs):
		category  = BookCategory.objects.create(
			name     = request.data["name"],
			charge = request.data["charge"])
		return Response(
			data   = BookCategorySerializer(category).data,
			status = status.HTTP_201_CREATED)

@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
class CategoryDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = BookCategory.objects.all()
	serializer_class = BookCategorySerializer


@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
class ListBooks(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

	def post(self,request, **kwargs):
		book  = Book.objects.create(
			bookname     = request.data["bookname"],
			category = BookCategory.objects.get(id=request.data["category"]),
			user     = User.objects.get(id=request.data["user"]))
		return Response(
			data   = BookSerializer(book).data,
			status = status.HTTP_201_CREATED)

@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
class BookDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer


@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
class ListRentedBooks(generics.ListCreateAPIView):
	queryset = RentedBook.objects.all()
	serializer_class = RentedBookCategorySerializer
	# permission_classes = (permissions.IsAuthenticated,IsOwner)

	def post(self,request, **kwargs):
		rentedbook  = RentedBook.objects.create(
			book  = Book.objects.get(id=request.data["book"]),
			user  = User.objects.get(id=request.data["user"]))
		return Response(
			data   = RentedBookCategorySerializer(rentedbook).data,
			status = status.HTTP_201_CREATED)


@authentication_classes((TokenAuthentication, SessionAuthentication, BasicAuthentication))
class rentedBookDetails(generics.RetrieveUpdateDestroyAPIView):
	queryset = RentedBook.objects.all()
	serializer_class = RentedBookCategorySerializer