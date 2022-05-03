from library.books.schema import BookQuery, BookMutation
from library.users.schema import UserQuery, UserMutation
import graphene
from graphene.types.field import Field
import graphql_jwt
from library.users.models import *

class Query(BookQuery, UserQuery, graphene.ObjectType):
	pass

class Mutation(BookMutation, UserMutation, graphene.ObjectType):

	# JWT MUTATIONS
	token_auth = graphql_jwt.ObtainJSONWebToken.Field()
	verify_token = graphql_jwt.Verify.Field()
	refresh_token = graphql_jwt.Refresh.Field()
	revoke_token = graphql_jwt.Revoke.Field()
	delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()
	delete_refresh_token_cookie = graphql_jwt.DeleteRefreshTokenCookie.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)