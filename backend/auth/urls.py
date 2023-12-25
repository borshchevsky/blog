from django.urls import path

from auth.views import AuthView

urlpatterns = [
    path('auth', AuthView.as_view()),
]
