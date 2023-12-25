from rest_framework.routers import DefaultRouter

from blog.views import CommentViewSet, PostViewSet

router = DefaultRouter()
router.register('post', PostViewSet)
router.register('comment', CommentViewSet)
