from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from .models import Service, ServiceCategory


@cache_page(60 * 15)
def services_list(request):
    """Services listing page"""
    category = request.GET.get('category')
    
    services = Service.objects.filter(is_active=True)
    
    if category:
        services = services.filter(category__slug=category)
    
    categories = ServiceCategory.objects.all()
    
    context = {
        'services': services,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'services/services_list.html', context)


def service_detail(request, slug):
    """Service detail page"""
    service = get_object_or_404(Service, slug=slug, is_active=True)
    related_services = Service.objects.filter(
        is_active=True, 
        category=service.category
    ).exclude(id=service.id)[:3]
    
    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/service_detail.html', context)
