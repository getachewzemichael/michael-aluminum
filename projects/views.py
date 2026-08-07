from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.db.models import Q
from .models import Project, ProjectCategory


@cache_page(60 * 15)
def projects_list(request):
    """Projects listing page with filtering"""
    category = request.GET.get('category')
    search = request.GET.get('q')
    
    projects = Project.objects.filter(is_active=True).exclude(static_featured='')
    
    if category:
        projects = projects.filter(category__slug=category)
    
    if search:
        projects = projects.filter(
            Q(title__icontains=search) | 
            Q(description__icontains=search) |
            Q(location__icontains=search)
        )
    
    categories = ProjectCategory.objects.all()
    
    context = {
        'projects': projects,
        'categories': categories,
        'selected_category': category,
        'search_query': search,
    }
    return render(request, 'projects/projects_list.html', context)


def project_detail(request, slug):
    """Project detail page"""
    project = get_object_or_404(Project, slug=slug, is_active=True)
    related_projects = Project.objects.filter(
        is_active=True,
        category=project.category
    ).exclude(id=project.id).exclude(static_featured='')[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
    }
    return render(request, 'projects/project_detail.html', context)
