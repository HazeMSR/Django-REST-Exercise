from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'', views.BookViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'booksauthor', views.BooksAuthorsViewSet)

urlpatterns = [
	path('', include(router.urls)),
]