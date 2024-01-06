# myapp/views.py

from rest_framework import generics, permissions
from rest_framework_simplejwt.views import TokenViewBase
from .serializers import UserSerializer
from django.contrib.auth import get_user_model

class SignUpView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

class LogoutView(TokenViewBase):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.logout(request)
