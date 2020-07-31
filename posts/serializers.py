from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    author_name = serializers.CharField(source='author.get_full_name',
                                        required=False)

    class Meta:
        fields = ('id',
                  'text',
                  'image',
                  'author',
                  'author_name',
                  'pub_date'
                  )
        model = Post
        read_only_fields = ['author', 'pub_date']


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    author_name = serializers.CharField(source='author.get_full_name',
                                        required=False)
    post = serializers.IntegerField(source='post_id', required=False)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ['author', 'created']
