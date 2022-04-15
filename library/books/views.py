from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from library.books.serializers import *
import base64
from rest_framework.response import Response
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser, JSONParser

# class ThingView(views.APIView):
#     parser_classes = (JSONParser, FormParser, MultiPartParser,)

#     def post(self, request):
#         name = request.data['name']
#         image = request.data['image']
#         sz = ThingSerializer(data=request.data)
#         print('SERIALIZER',sz)
#         response = Response()
#         response.data = {
#             'name': name,
#             #'image':
#         }
#         return response

#     permission_classes = []

class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all().order_by('id')
    serializer_class = ThingSerializer
    permission_classes = []

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = []

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = []

class BooksAuthorsViewSet(viewsets.ModelViewSet):
    queryset = BooksAuthors.objects.all()
    serializer_class = BooksAuthorsSerializer
    permission_classes = []