from django.urls import path
from .views import UserRegisterView, LoginUser, CheckOTP

urlpatterns = [
    path('register/', UserRegisterView.as_view()),
    path('login/', LoginUser.as_view()),
    path('checkotp/', CheckOTP.as_view()),
]
