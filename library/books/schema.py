import graphene
from graphene_django import DjangoObjectType
from graphene.types.field import Field
from library.books.models import *

class AuthorType(DjangoObjectType):
	class Meta:
		model = Author
		fields = ('id', 'name', 'last_name',)

class BookType(DjangoObjectType):
	class Meta:
		model = Book
		fields = '__all__'

class BookQuery(graphene.ObjectType):

	
	all_authors = graphene.List(AuthorType, first=graphene.Int(), skip=graphene.Int())
	book_by_name = graphene.Field(BookType, name=graphene.String(required=True))
	#books_by_author_id = graphene.List(AuthorsType, author_id=graphene.Int(required=True))

	def resolve_all_authors(root, info, first = None, skip = None):
		from django.contrib.auth.middleware import get_user
		from graphql_jwt.utils import get_payload, get_user_by_payload

		context = info.context

		print('info',dir(context))
		#print('GET_USER:', get_user(info))
		
		user = info.context.user
		#print('USER INFO:', user)
		print('IS AUTHENTICATED? ', user.is_authenticated)
		
		if not user.is_authenticated:
			raise Exception("Authentication credentials were not provided")

		authors = Author.objects.all()
		if skip is not None:
			authors = authors[:skip]
		if first is not None:
			authors = authors[first:]

		return authors

	def resolve_book_by_name(root, info, name):
		try:
			return Book.objects.get(name=name)
		except Book.DoesNotExist:
			return None

class UpsertAuthorMutation(graphene.Mutation):
	class Arguments:
		# The input arguments for this mutation
		id = graphene.ID()
		name = graphene.String(required=True)
		last_name = graphene.String()

	# The class attributes define the response of the mutation
	author = graphene.Field(AuthorType)
	status = graphene.String()

	@classmethod
	def mutate(cls, root, info, name, last_name, id = None):
		author = None
		if id is not None:
			try:
				author = Author.objects.get(pk=id)
				author.name = name
				author.last_name = last_name
				author.save()
			except Author.DoesNotExist:
				return cls( book = None, status = 'Author not found')
		else:
			author = Author.objects.create(name=name, last_name=last_name)
			author.save()
		# Notice we return an instance of this mutation
		return UpsertAuthorMutation(author=author)

class DeleteAuthorMutation(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        author = Author.objects.get(pk=kwargs["id"])
        author.delete()
        return cls(ok=True)

class Object1Input(graphene.InputObjectType):
	id = graphene.ID()
	name = graphene.String()

class AuthorsInput(graphene.InputObjectType):
	id = graphene.ID()
	name = graphene.String(required=True)
	last_name = graphene.String()
	# object1 = graphene.Field(Object1Input)

class UpsertBookMutation(graphene.Mutation):
	class Arguments:
		# The input arguments for this mutation
		id = graphene.ID()
		name = graphene.String(required=True)
		publish_year = graphene.Int()
		pages = graphene.Int(required=True, description='Number of pages')
		price = graphene.Decimal(required=True, description='Average price')
		created_at = graphene.DateTime()
		updated_at = graphene.DateTime()
		authors = graphene.List(AuthorsInput)
	# books_authors = models.OneToOneField(Author, through='BookAuthor')

	# The class attributes define the response of the mutation
	book = graphene.Field(BookType)
	status = graphene.String()
	#ok = graphene.Boolean()

	@classmethod
	def mutate(cls, root, info, **kwargs):

		print('info:',dir(info.context))
		print('headers:',info.context.headers)

		l_authors = []
		if 'authors' in kwargs:
			authors = kwargs.pop('authors')
			for author in authors:
				aux = None
				if 'id' in author:
					try:
						aux = Author.objects.get(pk=author['id'])
						aux.name = author['name']
						aux.last_name = author['last_name']
						aux.save()
					except Author.DoesNotExist:
						return cls( status = 'Author not found', book = None)
				else:
					aux = Author.objects.create(name=author['name'], last_name=author['last_name'])
					aux.save()
				l_authors.append(aux)
		
		if 'id' in kwargs:
			book = None
			try:
				book = Book.objects.get(pk=kwargs['id'])
				book.name = kwargs['name']
				book.pages = kwargs['pages']
				book.price = kwargs['price']
				if 'publish_year' in kwargs:
					book.publish_year = kwargs['publish_year']
				if 'created_at' in kwargs:
					book.created_at = kwargs['created_at']
				if 'updated_at' in kwargs:
					book.updated_at = kwargs['updated_at']
				book.save()
			except Book.DoesNotExist:
				return cls( book = None, status = 'Book not found')
		else:
			book = Book.objects.create(**kwargs)
			book.save()
			for author in l_authors:
				books_authors = BooksAuthors.objects.create(book=book, author=author)
				books_authors.save()
		# Notice we return an instance of this mutation
		return UpsertBookMutation(book = book, status = 'ok')

class BookMutation(graphene.ObjectType):
	# LIBRARY MUTATIONS
	upsert_author = UpsertAuthorMutation.Field()
	delete_author = DeleteAuthorMutation.Field()
	upsert_book = UpsertBookMutation.Field()