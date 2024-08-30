from django.urls import path
from .views import (
    PostSerializerListCreate,
    postserilizerRetrieveUpdateDestroyAPIView,
    UserSerializerListCreate,
    UserSerializerRetrieveUpdateDestroyAPIView
)

urlpatterns = [
    path('posts/', PostSerializerListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', postserilizerRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('users/', UserSerializerListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserSerializerRetrieveUpdateDestroyAPIView.as_view(), name='user-detail'),
]