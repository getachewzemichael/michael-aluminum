from django.db import models


class GalleryCategory(models.Model):
    """Gallery categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Gallery Category"
        verbose_name_plural = "Gallery Categories"
    
    def __str__(self):
        return self.name


class GalleryImage(models.Model):
    """Gallery images"""
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, related_name='images')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="gallery/")
    thumbnail = models.ImageField(upload_to="gallery/thumbnails/", blank=True)
    
    # Tags for filtering
    tags = models.CharField(max_length=255, blank=True, help_text="Comma-separated tags")
    
    # Admin
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-order', '-created_at']
        verbose_name = "Gallery Image"
        verbose_name_plural = "Gallery Images"
    
    def __str__(self):
        return self.title


class GalleryVideo(models.Model):
    """Gallery videos (Drone shots, etc.)"""
    category = models.ForeignKey(GalleryCategory, on_delete=models.SET_NULL, null=True, related_name='videos')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video_url = models.URLField(help_text="YouTube or Vimeo URL")
    thumbnail = models.ImageField(upload_to="gallery/video_thumbnails/", blank=True)
    
    # Admin
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-order', '-created_at']
        verbose_name = "Gallery Video"
        verbose_name_plural = "Gallery Videos"
    
    def __str__(self):
        return self.title
