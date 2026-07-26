from django.contrib import admin
from .models import ServiceCategory, Service, ServiceImage


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    ordering = ['order']


class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'is_featured', 'is_active', 'order')
    list_filter = ('category', 'is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active', 'order')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ServiceImageInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'description', 'short_description')
        }),
        ('Media', {
            'fields': ('image', 'icon')
        }),
        ('Details', {
            'fields': ('features', 'applications', 'benefits')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords')
        }),
        ('Settings', {
            'fields': ('order', 'is_featured', 'is_active')
        }),
    )
    ordering = ['order']
