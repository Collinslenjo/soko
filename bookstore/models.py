from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BookCategory(models.Model):
	name = models.CharField(max_length=256)
	charge = models.FloatField()
	minimumcharge = models.FloatField()
	minimumdays = models.IntegerField()
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} - {}".format(self.name,self.charge,self.createdAt,self.updatedAt)
	
	class Meta:
		db_table = 'tbl_book_categories'


class Book(models.Model):
	bookname = models.CharField(max_length=256)
	category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	createdAt = models.DateTimeField(auto_now_add=True)
	updatedAt = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} - {}".format(self.bookname,self.category,self.user,self.createdAt,self.updatedAt)
	
	class Meta:
		db_table = 'tbl_books'

class RentedBook(models.Model):
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	returned = models.BooleanField(default=False)
	dateBorrowed = models.DateTimeField(auto_now_add=True)
	dateReturned = models.DateTimeField(auto_now_add=False,null=True)

	def __str__(self):
		return "{} - {}".format(self.book,self.user,self.returned,self.dateBorrowed,self.dateReturned)
	
	class Meta:
		db_table = 'tbl_rented_books'