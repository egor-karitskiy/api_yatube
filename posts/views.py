from rest_framework import viewsets, permissions, exceptions
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404

from .models import Post, Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrReadOnly
                          ]

    def perform_create(self, serializer):
        print(serializer.get_fields())
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)
        else:
            raise exceptions.PermissionDenied(
                'Поститься разрешено только авторизованным пользователям'
            )


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly
                          ]
    queryset = Comment.objects.all()
    lookup_fields = ('post', 'id')

    def perform_create(self, serializer):
        get_object_or_404(Post.objects, pk=self.kwargs['p_id'])
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user,
                            post_id=self.kwargs['p_id']
                            )
        else:
            raise exceptions.PermissionDenied(
                'Комментировать разрешено только авторизованным пользователям'
            )

    def get_queryset(self):
        post_id = self.kwargs['p_id']
        queryset = Comment.objects.filter(post__id=post_id)
        return queryset
