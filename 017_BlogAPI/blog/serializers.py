from rest_framework import serializers
from .models import Category,Post

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        exclude = []


class PostSerializer(serializers.Serializer):

    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()
    class Meta:
        model = Post 
        exclude = []