from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Quotation


@require_http_methods(["GET", "POST"])
def request_quotation(request):
    """Request quotation page"""
    if request.method == 'POST':
        quotation = Quotation()
        quotation.full_name = request.POST.get('full_name')
        quotation.company = request.POST.get('company', '')
        quotation.email = request.POST.get('email')
        quotation.phone = request.POST.get('phone')
        quotation.service_needed = request.POST.get('service_needed')
        quotation.project_location = request.POST.get('project_location')
        quotation.project_description = request.POST.get('project_description')
        quotation.budget = request.POST.get('budget', '')
        
        # Handle expected completion date
        expected_date = request.POST.get('expected_completion_date')
        if expected_date:
            quotation.expected_completion_date = expected_date
        
        # Handle file uploads
        if 'drawings' in request.FILES:
            quotation.drawings = request.FILES['drawings']
        
        if 'additional_files' in request.FILES:
            quotation.additional_files = request.FILES['additional_files']
        
        quotation.save()
        
        # Send email to company
        try:
            send_mail(
                f'New Quotation Request from {quotation.full_name}',
                f'Service: {quotation.service_needed}\nLocation: {quotation.project_location}\nBudget: {quotation.budget}\n\nDescription: {quotation.project_description}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.COMPANY_EMAIL],
                fail_silently=True,
            )
        except:
            pass
        
        messages.success(request, 'Your quotation request has been submitted. We will get back to you soon!')
        return redirect('core:home')
    
    context = {}
    return render(request, 'quotations/request_quotation.html', context)
