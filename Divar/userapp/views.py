from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserSerializer, Otpserializer, OtploginSerializer
from rest_framework.generics import CreateAPIView
import random 
from django.core.cache import cache
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
from .models import CustomUser


class UserRegisterView(CreateAPIView):
    model = CustomUser
    serializer_class = UserSerializer

class LoginUser(APIView):
    def post(self, request):
        serializer = Otpserializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']
        user = CustomUser.objects.filter(phone_number=phone_number).first()
        if user:
            otp = random.randint(100000, 999999)
            cache.set(phone_number, otp, timeout=180)
            request.session['phone_number'] = phone_number
            #sms to user
        else:
            return Response({'message': 'Invalid OTP'}, status=status.HTTP_400_BAD_REQUEST)


class CheckOTP(APIView):
    def post(self, request):
        serializer = OtploginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = request.session.get('phone_number')
        otp = serializer.validated_data['input_otp']
        cached_otp = cache.get(phone_number)
        if otp == cached_otp:
            cache.delete(phone_number)
            user = CustomUser.objects.get(phone_number=phone_number)
            refresh_token = RefreshToken.for_user(user)
            access_token = AccessToken.for_user(user)
            return Response(
                {
                    "refresh_token" : str(refresh_token),
                    "access_token" : str(access_token)
                }
            )        
        else:
            return Response({'message': 'Invalid OTP'}, status=status)