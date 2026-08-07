from django.shortcuts import render, get_object_or_404
from .models import Service, ServiceCategory


def services_list(request):
    """Services listing page"""
    category = request.GET.get('category')

    services = Service.objects.select_related('category').filter(is_active=True)

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
    service = get_object_or_404(
        Service.objects.select_related('category'),
        slug=slug, is_active=True
    )
    related_services = Service.objects.select_related('category').filter(
        is_active=True,
        category=service.category
    ).exclude(id=service.id)[:3]

    context = {
        'service': service,
        'related_services': related_services,
    }
    return render(request, 'services/service_detail.html', context)
