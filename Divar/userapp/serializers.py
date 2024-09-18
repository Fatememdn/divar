from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    phone_number = serializers.CharField(max_length=11)
    address = serializers.CharField(max_length=1000)
    city = serializers.ChoiceField(choices=CustomUser.CITY_STATUS)
    gender = serializers.ChoiceField(choices=CustomUser.GENDER_CHOICES)


    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'phone_number', 'address', 'city', 'gender']

    def create(self, validated_data):
            user = CustomUser.objects.create(
                username = validated_data['username'],
                phone_number = validated_data['phone_number'],
                address = validated_data['address'],
                city = validated_data['city'],
                gender = validated_data['gender']
            )
            user.set_password(validated_data['password'])
            user.save()
            return user
 

class Otpserializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=6)

class OtploginSerializer(serializers.Serializer):
    input_otp = serializers.CharField(max_length=11)