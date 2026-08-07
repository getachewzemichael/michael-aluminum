from django.db import models
from django.utils.text import slugify


class ServiceCategory(models.Model):
    """Service categories"""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Service Category"
        verbose_name_plural = "Service Categories"
    
    def __str__(self):
        return self.name


class Service(models.Model):
    """Main services offered"""
    category = models.ForeignKey(ServiceCategory, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    short_description = models.CharField(max_length=300, blank=True)
    
    # Media
    image = models.ImageField(upload_to="services/", blank=True, null=True)
    static_image = models.CharField(max_length=255, blank=True, help_text="Path relative to static folder e.g. images/Category 1 Handrail/photo.jpg")
    icon = models.CharField(max_length=100, help_text="Bootstrap icon class e.g. bi bi-building", blank=True)
    
    # Details
    features = models.TextField(help_text="Features separated by newline", blank=True)
    applications = models.TextField(help_text="Applications separated by newline", blank=True)
    benefits = models.TextField(help_text="Benefits separated by newline", blank=True)
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    
    # Admin
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Service"
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_features_list(self):
        return [f.strip() for f in self.features.split('\n') if f.strip()]
    
    def get_applications_list(self):
        return [a.strip() for a in self.applications.split('\n') if a.strip()]
    
    def get_benefits_list(self):
        return [b.strip() for b in self.benefits.split('\n') if b.strip()]


class ServiceImage(models.Model):
    """Additional images for services"""
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to="services/gallery/")
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.service.title} - Image {self.order}"
