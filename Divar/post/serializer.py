from .models import *
from rest_framework.serializers import ModelSerializer


class PostSerializers(ModelSerializer):
    model = Post
    fields = "__al__"

class UserSerializers(ModelSerializer):
    model = Post
    fields = "__al__"