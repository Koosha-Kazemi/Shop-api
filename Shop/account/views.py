from rest_framework import generics
from rest_framework.response import Response

from django.contrib.auth import get_user_model

from rest_framework_simplejwt.tokens import RefreshToken

from .serializer import RegisterUserSerializer

User = get_user_model()

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        refresh_token = RefreshToken.for_user(request.user)


        return Response({
                'refresh_token' : str(refresh_token),
                'access_token' : str(refresh_token.access_token)
            })