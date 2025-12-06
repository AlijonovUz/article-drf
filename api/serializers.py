from rest_framework import serializers

from accounts.serializers import UpdateProfileSerializer
from .models import Category, Article


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ("id",)


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
        read_only_fields = ("id", "author")

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["author"] = UpdateProfileSerializer(instance.author).data
        data["category"] = CategorySerializer(instance.category).data

        return data
