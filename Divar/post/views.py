from rest_framework.generics import CreateAPIView,RetrieveAPIView, DestroyAPIView, ListAPIView
from .models import Post
from .serializers import PostSerializers   
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class PostCreateView(CreateAPIView):
    permission_classes =  [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes =  [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['price']
    search_fields = ['category__name']
    filterset_fields = ['category__name', 'title']

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    permission_classes =  [IsAuthenticated]

class PostDeleteView(DestroyAPIView):
    permission_classes =  [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializers