from django.shortcuts import render, get_object_or_404
from django.views.decorators.cache import cache_page
from django.db.models import Q
from .models import BlogPost, BlogCategory


@cache_page(60 * 15)
def blog_list(request):
    """Blog listing page"""
    category = request.GET.get('category')
    search = request.GET.get('q')
    
    posts = BlogPost.objects.filter(is_published=True)
    
    if category:
        posts = posts.filter(category__slug=category)
    
    if search:
        posts = posts.filter(
            Q(title__icontains=search) |
            Q(content__icontains=search) |
            Q(excerpt__icontains=search)
        )
    
    categories = BlogCategory.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
        'selected_category': category,
        'search_query': search,
    }
    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    """Blog post detail page"""
    post = get_object_or_404(BlogPost, slug=slug, is_published=True)
    
    # Increment view count
    post.views_count += 1
    post.save(update_fields=['views_count'])
    
    # Get related posts
    related_posts = BlogPost.objects.filter(
        is_published=True,
        category=post.category
    ).exclude(id=post.id)[:3]
    
    context = {
        'post': post,
        'related_posts': related_posts,
    }
    return render(request, 'blog/blog_detail.html', context)
