from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User
from .validators import validate_user_data
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny

# Create your views here.
class UserCreateView(APIView):
    def post(self, request):
        
        permission_classes = [AllowAny]
        
        rlt_message = validate_user_data(request.data)
        
        if rlt_message is not None:
            return Response({"message":rlt_message}, status=400)
        
        # user = User.objects.create_user(
        #     username = request.data.get("username"),
        #     password = request.data.get("password"),
        #     nickname = request.data.get("nickname"),
        #     birth = request.data.get("birth"),
        #     first_name = request.data.get("first_name"),
        #     last_name = request.data.get("last_name"),
        #     email = request.data.get("email"),
        # )
        
        user = User.objects.create_user(**request.data)
        
        # refresh = RefreshToken.for_user(user)

        # return Response({
        #     'refresh': str(refresh),
        #     'access': str(refresh.access_token),
        # })
        
        serializer = UserSerializer(user)
        Response_dict = serializer.data
        # Response_dict['access'] = str(refresh.access_token),
        # Response_dict['refresh'] = str(refresh),
        
        return Response(serializer.data)
    
class UserLoginView(APIView):
    
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username,password=password)
        if not user :
            return Response(
                {"message": "id or password incorrect"},   
                status=400            
            )    
        
        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        
class UserProfileView(APIView):
    def get(self, request, username):
        #user check
        user = User.objects.get(username=username)
        
        #user serializer
        serializer = UserProfileView(user)
        return Response(serializer.data)
        