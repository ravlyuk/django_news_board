from rest_framework import serializers
from .models import Bb, Comment


# NEWS
class NewsListSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = (
            "title",
            "content",
            "name_author",
            "rubric",
            "published",
            "likes",
        )


class NewsListDetailSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = (
            "title",
            "content",
            "name_author",
            "rubric",
            "published",
        )


class NewsVoiceSerializer(serializers.ModelSerializer):
    id_news = serializers.Field(source="has_expired",)

    class Meta:
        model = Bb
        fields = ("id_news",)


# COMMENTS
class CommentListDetailSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "name",
            "content",
            "post",
            "published",
        )
