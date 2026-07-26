from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Count


@staff_member_required
def dashboard(request):
    """Admin dashboard"""
    from projects.models import Project
    from services.models import Service
    from testimonials.models import Testimonial
    from quotations.models import Quotation
    from contact.models import ContactMessage
    from careers.models import JobApplication
    from blog.models import BlogPost
    
    context = {
        'total_projects': Project.objects.count(),
        'total_services': Service.objects.count(),
        'total_testimonials': Testimonial.objects.count(),
        'pending_quotations': Quotation.objects.filter(status='pending').count(),
        'new_messages': ContactMessage.objects.filter(status='new').count(),
        'pending_applications': JobApplication.objects.filter(status='applied').count(),
        'published_posts': BlogPost.objects.filter(is_published=True).count(),
    }
    return render(request, 'dashboard/dashboard.html', context)
