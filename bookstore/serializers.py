from rest_framework import serializers
from .models import *

class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ("id","bookname", "category","user","createdAt","updatedAt")

class BookCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = BookCategory
		fields = ("id","name", "charge","createdAt","updatedAt")

class RentedBookCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = RentedBook
		fields = ("id","book", "user", "returned","dateBorrowed","dateReturned")