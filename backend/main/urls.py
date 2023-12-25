from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from auth.urls import urlpatterns as auth_urlpatterns
from blog.urls import router as blog_router

urlpatterns = [
                  path('api/v1/', include(auth_urlpatterns + blog_router.urls)),
                  path('admin/', admin.site.urls),
              ] + staticfiles_urlpatterns()
