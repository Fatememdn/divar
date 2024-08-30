from django.shortcuts import render
from .serializer import PostSerializers, UserSerializers
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post, User

class postserilizerlistcreate(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class postserilizerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class UserSerializerListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class UserSerializerRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
