from . import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'library',views.LibraryViewSet)
router.register(r'employee',views.EmployeeViewSet)
router.register(r'thing',views.ThingViewSet)
router.register(r'author', views.AuthorViewSet)
router.register(r'booksauthor', views.BooksAuthorsViewSet)
router.register(r'', views.BookViewSet)

urlpatterns = [
	#path('thing', views.ThingView.as_view()),
	path('', include(router.urls)),
]