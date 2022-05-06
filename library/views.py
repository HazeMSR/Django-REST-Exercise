from library import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    # Replace the serializer with your custom
    serializer_class = serializers.CustomTokenObtainPairSerializer