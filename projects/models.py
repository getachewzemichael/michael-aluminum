from django.db import models
from django.utils.text import slugify


class ProjectCategory(models.Model):
    """Project categories"""
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=100, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Project Category"
        verbose_name_plural = "Project Categories"
    
    def __str__(self):
        return self.name


class Project(models.Model):
    """Portfolio projects"""
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, related_name='projects')
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    
    # Images
    featured_image = models.ImageField(upload_to="projects/featured/", blank=True, null=True)
    before_image = models.ImageField(upload_to="projects/before/", blank=True, null=True)
    after_image = models.ImageField(upload_to="projects/after/", blank=True, null=True)

    # Static image paths (persistent on Render free plan)
    static_featured = models.CharField(max_length=255, blank=True)
    static_before = models.CharField(max_length=255, blank=True)
    static_after = models.CharField(max_length=255, blank=True)
    
    # Project Details
    location = models.CharField(max_length=300)
    client = models.CharField(max_length=200)
    year = models.IntegerField()
    duration = models.CharField(max_length=100, blank=True, help_text="e.g., 6 months")
    
    # Technical Details
    materials_used = models.TextField(help_text="Materials separated by newline")
    challenges = models.TextField(blank=True)
    solutions = models.TextField(blank=True)
    results = models.TextField(blank=True)
    
    # Client Feedback
    client_feedback = models.TextField(blank=True)
    client_rating = models.IntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)])
    
    # SEO
    meta_description = models.CharField(max_length=160, blank=True)
    meta_keywords = models.CharField(max_length=255, blank=True)
    
    # Admin
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-year', '-order']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    def get_materials_list(self):
        return [m.strip() for m in self.materials_used.split('\n') if m.strip()]


class ProjectImage(models.Model):
    """Gallery images for projects"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ImageField(upload_to="projects/gallery/")
    caption = models.CharField(max_length=200, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Project Image"
        verbose_name_plural = "Project Images"
    
    def __str__(self):
        return f"{self.project.title} - Image {self.order}"


class ProjectVideo(models.Model):
    """Video gallery for projects"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='videos')
    title = models.CharField(max_length=200)
    video_url = models.URLField(help_text="YouTube or Vimeo URL")
    thumbnail = models.ImageField(upload_to="projects/videos/", blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Project Video"
        verbose_name_plural = "Project Videos"
    
    def __str__(self):
        return f"{self.project.title} - {self.title}"
