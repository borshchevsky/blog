from django.urls import path

from auth.views import AuthView, RegisterView

urlpatterns = [
    path('auth', AuthView.as_view()),
    path('register', RegisterView.as_view()),
]
