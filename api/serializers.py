from rest_framework import serializers

from posts.models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name',
                                        required=False)
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username',
                                          required=False)
    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ['author', 'pub_date', 'author_name']


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.get_full_name',
                                        required=False
                                        )
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username',
                                          required=False)
    post = serializers.IntegerField(source='post.id',
                                    required=False,
                                    read_only=True
                                    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ['author', 'created', 'author_name']
