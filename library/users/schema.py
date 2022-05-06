import graphene
from graphene_django import DjangoObjectType
from graphene.types.field import Field
from library.users.models import *

class UserType(DjangoObjectType):
 	class Meta:
 		model = User
 		fields = '__all__'

class UserQuery(graphene.ObjectType):
	all_users = graphene.List(UserType, first=graphene.Int(), skip=graphene.Int())

	def resolve_all_users(root, info, first = None, skip = None):
		users = User.objects.all()
		if skip is not None:
			users = users[:skip]
		if first is not None:
			users = users[first:]

		return users

class UpsertUserMutation(graphene.Mutation):
	class Arguments:
		# The input arguments for this mutation
		id = graphene.ID()
		username = graphene.String()
		email = graphene.String(required=True)
		password = graphene.String(required=True)
		mode = graphene.Int()

	# The class attributes define the response of the mutation
	user = graphene.Field(UserType)
	status = graphene.String()

	@classmethod
	def mutate(cls, root, info, **kwargs):
		user = None
		if 'id' in kwargs:
			try:
				user = User.objects.get(pk=kwargs.pop('id'))
				user.username = kwargs.pop('username')
				user.email = kwargs.pop('email')
				user.password = kwargs.pop('password')
				if 'mode' in kwargs:
					user.mode = kwargs.pop('mode')
				user.save()
			except User.DoesNotExist:
				return cls( user = None, status = 'User not found')
		else:
			user = User.objects.create(**kwargs)
			user.save()
		# Notice we return an instance of this mutation
		return UpsertUserMutation(user=user)

class UserMutation(graphene.ObjectType):
	# USERS MUTATIONS
	upsert_user = UpsertUserMutation.Field()