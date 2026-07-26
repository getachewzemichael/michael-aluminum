from django.contrib import admin
from .models import ProjectCategory, Project, ProjectImage, ProjectVideo


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ['order']


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1


class ProjectVideoInline(admin.TabularInline):
    model = ProjectVideo
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'location', 'year', 'is_featured', 'is_active')
    list_filter = ('category', 'year', 'is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active')
    search_fields = ('title', 'description', 'location')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProjectImageInline, ProjectVideoInline]
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'category', 'description')
        }),
        ('Images', {
            'fields': ('featured_image', 'before_image', 'after_image')
        }),
        ('Project Details', {
            'fields': ('location', 'client', 'year', 'duration', 'materials_used')
        }),
        ('Technical Details', {
            'fields': ('challenges', 'solutions', 'results')
        }),
        ('Client Feedback', {
            'fields': ('client_feedback', 'client_rating')
        }),
        ('SEO', {
            'fields': ('meta_description', 'meta_keywords')
        }),
        ('Settings', {
            'fields': ('is_featured', 'is_active', 'order')
        }),
    )
    ordering = ['-year']
