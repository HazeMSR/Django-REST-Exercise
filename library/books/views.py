from rest_framework import viewsets
from rest_framework import views
from rest_framework import permissions
from library.books.serializers import *
import base64
from rest_framework.response import Response
from rest_framework.parsers import FormParser, FileUploadParser, MultiPartParser, JSONParser
from rest_framework import pagination
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
from django.views.decorators.vary import vary_on_cookie
from django.views.decorators.vary import vary_on_headers

from rest_framework import status

class CustomPagination(pagination.PageNumberPagination):
    page_size = 2
    page_size_query_param = 'size'
    max_page_size = 100
    page_query_param = 'p'

class CustomPaginationOffset(pagination.LimitOffsetPagination):
    default_limit = 2
    limit_query_param = 'l'
    offset_query_param = 'o'
    max_limit = 100

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('id')
    serializer_class = LibrarySerializer
    permission_classes = []
    
    # Overriding list method to return only the ID of the library that are greater than Zero
    @method_decorator(vary_on_headers('Authorization',))
    @method_decorator(cache_page(60*60, key_prefix='main'))
    def list(self, request):
        library_queryset = Library.objects.filter(id__gt = 0)
        # Try to play with the above line for example:
        # library_queryset = Library.objects.filter(id__lte = request.library_id)
        # Using that line it will use a parameter called "library_id" of your request
        # in order to retrieve all the libraries that contains an ID less than equal (<=)
        # of the library_id parameter

        serializer = LibrarySerializer(library_queryset, many = True)
        return Response(serializer.data)
    
    # You can also override the other methods and also you can use the PRIMARY KEY passed at the end of the URL request
    def retrieve(self, request, pk=None):
        library_queryset = Library.objects.filter(id = pk)
        serializer = LibrarySerializer(library_queryset)
        return Response(serializer.data)

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('id')
    serializer_class = EmployeeSerializer
    permission_classes = []

class ThingViewSet(viewsets.ModelViewSet):
    queryset = Thing.objects.all().order_by('id')
    serializer_class = ThingSerializer
    permission_classes = []


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = AuthorSerializer
    permission_classes = []
    # pagination_class = CustomPaginationOffset
    
    # @method_decorator(vary_on_cookie)
    # @method_decorator(cache_page(60*60, key_prefix='author'), name='dispatch')
    # def create(self, request):
    #     print('c1:',cache.get('author'))
    #     print('c2:',cache.get('dispatch'))
        
    #     if 'author' in cache:
    #         print('-----AUTHOR----')
    #     if 'dispatch' in cache:
    #         print('-----DISPATCH----')
    #     if 'default' in cache:
    #         print('DEFAULT')
    #     cache.set('author')
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(serializer.data, status=status.HTTP_201_CREATED)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = []

class BooksAuthorsViewSet(viewsets.ModelViewSet):
    queryset = BooksAuthors.objects.all()
    serializer_class = BooksAuthorsSerializer
    permission_classes = []