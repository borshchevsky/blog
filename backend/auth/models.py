from uuid import uuid4

from django.db import models


class Token(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    token = models.CharField(max_length=255)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
