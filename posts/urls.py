from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as fwv

from posts.views import PostViewSet, CommentViewSet


router = DefaultRouter()
router.register('api/v1/posts', PostViewSet)
router.register(r'api/v1/posts/(?P<p_id>\d+)/comments',
                CommentViewSet)

urlpatterns = [
    path('api/v1/api-token-auth/', fwv.obtain_auth_token),
    path('', include(router.urls)),

]
