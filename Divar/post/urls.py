from django.urls import path
from .views import PostCreateView, PostListView, PostDetailView, PostDeleteView

urlpatterns = [
    path('create/', PostCreateView.as_view()),
    path('list/', PostListView.as_view()),
    path('detail/<int:pk>/', PostDetailView.as_view()),
    path('delete/<int:pk>/', PostDeleteView.as_view()),
]