from django.contrib import admin
from .models import CompanyInfo, SiteSettings, StatisticCard, WhyChooseUsCard


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'updated_at')
    fieldsets = (
        ('Company Information', {
            'fields': ('name', 'tagline', 'description', 'logo', 'favicon')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'whatsapp', 'telegram', 'address', 'city', 'country')
        }),
        ('Social Media', {
            'fields': ('facebook', 'instagram', 'linkedin', 'youtube', 'tiktok')
        }),
        ('Statistics', {
            'fields': ('years_experience', 'projects_completed', 'happy_clients', 'team_members')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords')
        }),
    )


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('updated_at',)


@admin.register(StatisticCard)
class StatisticCardAdmin(admin.ModelAdmin):
    list_display = ('value', 'title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ['order']


@admin.register(WhyChooseUsCard)
class WhyChooseUsCardAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    ordering = ['order']
