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
	all_authors = graphene.List(AuthorType)
	book_by_name = graphene.Field(BookType, name=graphene.String(required=True))
	#books_by_author_id = graphene.List(AuthorsType, author_id=graphene.Int(required=True))

	def resolve_all_authors(root, info):
		return Author.objects.all()

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

	@classmethod
	def mutate(cls, root, info, name, last_name, id = None):
		author = None
		if id is not None:
			author = Author.objects.get(pk=id)
			author.name = name
			author.last_name = last_name
			author.save()
		else:
			author = Author.objects.create(name=name, last_name=last_name)
			author.save()
		# Notice we return an instance of this mutation
		return AuthorMutation(author=author)

class DeleteAuthorMutation(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        author = Author.objects.get(pk=kwargs["id"])
        author.delete()
        return cls(ok=True)

class Query(BookQuery, graphene.ObjectType):
	pass

class Mutation(graphene.ObjectType):
	upsert_author = UpsertAuthorMutation.Field()
	delete_author = DeleteAuthorMutation.Field()
	#update_book = BookMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)