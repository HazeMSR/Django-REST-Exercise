from django.db import models

class Library(models.Model):
	name = models.CharField(max_length=128)

class Employee(models.Model):
	name = models.CharField(max_length=128)
	library = models.ForeignKey(Library, related_name='employees', on_delete=models.CASCADE)

class Thing(models.Model):
	name = models.CharField(max_length=128)
	image = models.TextField(null=False)

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=128)
	last_name = models.CharField(max_length=128, null=True)

class Book(models.Model):
	name = models.CharField(max_length = 256)
	publish_year = models.SmallIntegerField()
	pages = models.SmallIntegerField()
	price = models.DecimalField(max_digits = 6, decimal_places = 2)
	created_at = models.DateTimeField(auto_now_add=True, null=True)
	updated_at = models.DateTimeField(auto_now=True,null=True)
	authors = models.ManyToManyField(Author, through='BooksAuthors')
	# books_authors = models.OneToOneField(Author, through='BookAuthor')

	updated_at = models.DateTimeField(auto_now=True,null=True)

# class BookAuthor(models.Model):
class BooksAuthors(models.Model):
	book = models.ForeignKey(Book, related_name='BookWithAuthors', on_delete=models.DO_NOTHING)
	author = models.ForeignKey(Author, related_name='AuthorWithBooks', on_delete=models.DO_NOTHING)

	def __str__(self):
		return f'{self.id}'

