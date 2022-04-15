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
class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('id')
    serializer_class = LibrarySerializer
    permission_classes = []
    
    # Overriding list method to return only the ID of the library that are greater than Zero
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