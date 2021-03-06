from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as fwv

from api.views import PostViewSet, CommentViewSet


router = DefaultRouter()
router.register('v1/posts', PostViewSet)
router.register(r'v1/posts/(?P<p_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('v1/api-token-auth/', fwv.obtain_auth_token),
    path('', include(router.urls)),

]
