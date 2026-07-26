from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'phone', 'is_vendor')
    list_filter = ('is_vendor', 'created_at')
    search_fields = ('user__username', 'company', 'phone')
    readonly_fields = ('created_at', 'updated_at')
