from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from .models import JobPosition, JobApplication
from django.core.mail import send_mail
from django.conf import settings


@cache_page(60 * 15)
def careers_list(request):
    """Careers/Jobs page"""
    jobs = JobPosition.objects.filter(status='open')
    
    context = {
        'jobs': jobs,
    }
    return render(request, 'careers/careers_list.html', context)


def job_detail(request, slug):
    """Job details page"""
    job = get_object_or_404(JobPosition, slug=slug, status='open')
    
    context = {
        'job': job,
    }
    return render(request, 'careers/job_detail.html', context)


@require_http_methods(["GET", "POST"])
def apply_job(request, slug):
    """Job application page"""
    job = get_object_or_404(JobPosition, slug=slug, status='open')
    
    if request.method == 'POST':
        application = JobApplication(job_position=job)
        application.full_name = request.POST.get('full_name')
        application.email = request.POST.get('email')
        application.phone = request.POST.get('phone')
        application.cover_letter = request.POST.get('cover_letter')
        
        if 'cv' in request.FILES:
            application.cv = request.FILES['cv']
        
        application.portfolio_link = request.POST.get('portfolio_link', '')
        application.linkedin_profile = request.POST.get('linkedin_profile', '')
        
        application.save()
        
        # Send confirmation email
        try:
            send_mail(
                f'Application Received - {job.title}',
                f'Thank you for applying for {job.title} position. We will review your application and get back to you soon.',
                settings.DEFAULT_FROM_EMAIL,
                [application.email],
                fail_silently=True,
            )
        except:
            pass
        
        messages.success(request, 'Your application has been submitted successfully!')
        return redirect('careers:list')
    
    context = {
        'job': job,
    }
    return render(request, 'careers/apply_job.html', context)
