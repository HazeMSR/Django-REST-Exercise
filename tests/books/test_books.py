import pytest
from library.books.models import *


@pytest.mark.django_db
@pytest.mark.parametrize(
	'nombre, apellido',
	(
		('Paulo','Coelho'),
		('Haruki','Murakami'),
		('Jordi','Rosado')
	)
)
def test_author_name(nombre, apellido):
	author = Author.objects.create(name=nombre, last_name=apellido)
	print('This is my authors name: ',author.name)
	# assert author.last_name == 'Coelho'
	assert Author.objects.all().count() == 1
	author.delete()
	assert Author.objects.all().count() < 1

@pytest.mark.django_db
def test_author_with_monkey(monkeypatch):

	author = Author.objects.create(name='nombre', last_name='apellido')
	
	class AuthorQuerysetMock():
		def __init__(self):
			self.some_value=1
		
		def count(self):
			return 4

	def model_count_mock():
		return AuthorQuerysetMock()

	monkeypatch.setattr(Author.objects, 'all', model_count_mock)

	assert Author.objects.all().count() == 4
	print('Haciendo el monkeypatch')