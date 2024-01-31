from django.contrib import admin

from auth.models import Token, User

admin.site.register(Token)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['is_email_verified']

    def is_email_verified(self):
        return self.profile.is_email_verifiedZ
