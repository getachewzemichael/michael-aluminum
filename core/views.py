from django.shortcuts import render
from .models import CompanyInfo, StatisticCard, WhyChooseUsCard
from services.models import Service
from projects.models import Project
from testimonials.models import Testimonial
from blog.models import BlogPost


def home(request):
    """Home page with hero, services, projects, and testimonials"""
    context = {
        'company_info': CompanyInfo.objects.first(),
        'statistics': StatisticCard.objects.filter(is_active=True),
        'services': Service.objects.filter(is_active=True)[:6],
        'projects': Project.objects.filter(is_active=True).exclude(featured_image__isnull=True).exclude(featured_image='')[:6],
        'testimonials': Testimonial.objects.filter(is_active=True)[:6],
        'blog_posts': BlogPost.objects.filter(is_published=True)[:3],
        'why_choose_us': WhyChooseUsCard.objects.filter(is_active=True),
    }
    return render(request, 'core/home.html', context)


def about(request):
    """About page"""
    context = {
        'company_info': CompanyInfo.objects.first(),
        'why_choose_us': WhyChooseUsCard.objects.filter(is_active=True),
    }
    return render(request, 'core/about.html', context)


from django.http import JsonResponse


def health(request):
    """Lightweight health check endpoint for uptime monitoring"""
    return JsonResponse({'status': 'ok'})


def terms(request):
    """Terms of Service page"""
    return render(request, 'core/terms.html')


def privacy(request):
    """Privacy Policy page"""
    return render(request, 'core/privacy.html')
