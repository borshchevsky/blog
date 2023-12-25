from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include

from blog.urls import router

urlpatterns = [
                  path('api/v1/', include(router.urls)),
                  path('admin/', admin.site.urls),
              ] + staticfiles_urlpatterns()
