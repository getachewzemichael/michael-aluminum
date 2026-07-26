from django.contrib import admin
from .models import Testimonial


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_company', 'rating', 'is_featured', 'is_active')
    list_filter = ('rating', 'is_featured', 'is_active')
    list_editable = ('is_featured', 'is_active')
    search_fields = ('client_name', 'client_company', 'review')
    ordering = ['-is_featured', '-order']
