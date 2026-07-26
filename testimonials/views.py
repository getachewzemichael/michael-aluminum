from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Testimonial


@cache_page(60 * 15)
def testimonials_list(request):
    """Testimonials page"""
    featured = Testimonial.objects.filter(is_active=True, is_featured=True)
    all_testimonials = Testimonial.objects.filter(is_active=True)
    
    context = {
        'featured_testimonials': featured,
        'testimonials': all_testimonials,
    }
    return render(request, 'testimonials/testimonials_list.html', context)
