from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name',
                                        required=False)
    author = serializers.CharField(source='author.username',
                                   required=False)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ['author', 'pub_date', 'author_name']


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name',
                                        required=False)
    author = serializers.CharField(source='author.username',
                                   required=False)
    post = serializers.IntegerField(source='post_id', required=False)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ['author', 'created', 'author_name']
