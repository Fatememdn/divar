from rest_framework.generics import CreateAPIView,RetrieveAPIView, DestroyAPIView, ListAPIView
from .models import Post
from .serializers import PostSerializers   

class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostDetailView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class PostDeleteView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers