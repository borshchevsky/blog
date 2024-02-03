from django.urls import path
from rest_framework.routers import DefaultRouter

from auth.views import AuthView, RegisterView, UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet)

urlpatterns = [
                  path('auth', AuthView.as_view()),
                  path('register', RegisterView.as_view()),
              ] + router.urls
