from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status , permissions
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth  import authenticate
from .models import User
# Create your views here.

class UserSignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'user':{
                        'id':user.id, 
                        'email':user.email , 
                        'name': user.name,
                    }, 
                    'refresh':str(refresh), 
                    'access':str(refresh.access_token),
                }, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    permissinon_classes = [permissions.AllowAny]

    def post(self,request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request,email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'user':{
                    'id':user.id, 
                    'email':user.email ,
                    "name":user.name,
                    },
                    'refresh': str(refresh),
                    'access':str(refresh.access_token),

            },status= status.HTTP_200_OK)
        return Response({"detail" : "Invalid Credentials"}, status=status.HTTP_401_UNAUTHORIZED)


