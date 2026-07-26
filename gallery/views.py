from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import GalleryImage, GalleryVideo, GalleryCategory


@cache_page(60 * 15)
def gallery_list(request):
    """Gallery page with images and videos"""
    category = request.GET.get('category')
    
    images = GalleryImage.objects.all()
    videos = GalleryVideo.objects.all()
    categories = GalleryCategory.objects.all()
    
    if category:
        images = images.filter(category__slug=category)
        videos = videos.filter(category__slug=category)
    
    context = {
        'images': images,
        'videos': videos,
        'categories': categories,
        'selected_category': category,
    }
    return render(request, 'gallery/gallery_list.html', context)
