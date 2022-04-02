from users import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
	path('', include(router.urls)),
]