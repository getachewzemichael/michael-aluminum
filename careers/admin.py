from django.contrib import admin
from .models import JobPosition, JobApplication


class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    extra = 0
    readonly_fields = ('applied_at', 'updated_at')


@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'employment_type', 'status', 'is_featured')
    list_filter = ('status', 'employment_type', 'department', 'posted_date')
    list_editable = ('is_featured',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [JobApplicationInline]
    fieldsets = (
        ('Position Information', {
            'fields': ('title', 'slug', 'department', 'employment_type')
        }),
        ('Description', {
            'fields': ('description', 'requirements', 'responsibilities', 'benefits')
        }),
        ('Details', {
            'fields': ('location', 'salary_range')
        }),
        ('Admin', {
            'fields': ('status', 'is_featured', 'closing_date')
        }),
    )
    ordering = ['-posted_date']


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'job_position', 'email', 'status', 'applied_at')
    list_filter = ('status', 'applied_at', 'job_position')
    search_fields = ('full_name', 'email', 'job_position__title')
    list_editable = ('status',)
    fieldsets = (
        ('Applicant Information', {
            'fields': ('full_name', 'email', 'phone')
        }),
        ('Job Position', {
            'fields': ('job_position',)
        }),
        ('Application', {
            'fields': ('cover_letter', 'cv', 'portfolio_link', 'linkedin_profile')
        }),
        ('Admin', {
            'fields': ('status', 'notes')
        }),
    )
    readonly_fields = ('applied_at', 'updated_at')
    ordering = ['-applied_at']
