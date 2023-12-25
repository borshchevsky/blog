from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from auth.views import CustomAuthentication
from blog.models import Post, Comment
from blog.serializers import PostSerializer, CommentSerializer


class PostViewSet(ModelViewSet):
    authentication_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
