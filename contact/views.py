from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from .models import ContactMessage, Newsletter


@require_http_methods(["GET", "POST"])
def contact(request):
    """Contact page"""
    if request.method == 'POST':
        message = ContactMessage()
        message.name = request.POST.get('name')
        message.email = request.POST.get('email')
        message.phone = request.POST.get('phone', '')
        message.subject = request.POST.get('subject')
        message.message = request.POST.get('message')
        
        message.save()
        
        # Send email to company
        try:
            send_mail(
                f'New Contact Message: {message.subject}',
                f'From: {message.name} ({message.email})\n\n{message.message}',
                settings.DEFAULT_FROM_EMAIL,
                [settings.COMPANY_EMAIL],
                fail_silently=True,
            )
        except:
            pass
        
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact:contact')
    
    context = {
        'company_info': None,
    }
    return render(request, 'contact/contact.html', context)


def newsletter_subscribe(request):
    """Newsletter subscription"""
    if request.method == 'POST':
        email = request.POST.get('email')
        
        try:
            subscription, created = Newsletter.objects.get_or_create(email=email)
            
            if created:
                messages.success(request, 'Thank you for subscribing!')
            else:
                messages.info(request, 'You are already subscribed.')
            
            return redirect(request.META.get('HTTP_REFERER', '/'))
        except Exception as e:
            messages.error(request, 'An error occurred. Please try again.')
            return redirect(request.META.get('HTTP_REFERER', '/'))
    
    return redirect('/')
