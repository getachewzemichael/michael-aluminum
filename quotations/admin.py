from django.contrib import admin
from .models import Quotation, QuotationResponse


class QuotationResponseInline(admin.TabularInline):
    model = QuotationResponse
    extra = 0
    readonly_fields = ('created_at', 'updated_at')


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'service_needed', 'status', 'created_at')
    list_filter = ('status', 'created_at', 'service_needed')
    search_fields = ('full_name', 'email', 'company', 'project_description')
    fieldsets = (
        ('Personal Information', {
            'fields': ('full_name', 'company', 'email', 'phone')
        }),
        ('Project Details', {
            'fields': ('service_needed', 'project_location', 'project_description')
        }),
        ('Budget and Timeline', {
            'fields': ('budget', 'expected_completion_date')
        }),
        ('Attachments', {
            'fields': ('drawings', 'additional_files')
        }),
        ('Admin', {
            'fields': ('status', 'assigned_to', 'notes')
        }),
    )
    inlines = [QuotationResponseInline]
    ordering = ['-created_at']
    readonly_fields = ('created_at', 'updated_at')


@admin.register(QuotationResponse)
class QuotationResponseAdmin(admin.ModelAdmin):
    list_display = ('quote_number', 'quotation', 'quote_amount', 'delivery_date')
    list_filter = ('currency', 'delivery_date')
    search_fields = ('quote_number', 'description')
    readonly_fields = ('created_at', 'updated_at')
