from django.contrib import admin
from .models import User, UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'Profile'

class UserAdmin(admin.ModelAdmin):
    inlines = (UserProfileInline,)
    list_display = ('username', 'email', 'is_artist', 'is_admin', 'is_visitor', 'is_client')
    search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)
