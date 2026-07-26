from django.db import models


class Testimonial(models.Model):
    """Client testimonials"""
    client_name = models.CharField(max_length=200)
    client_title = models.CharField(max_length=200, blank=True, help_text="e.g., Project Manager")
    client_company = models.CharField(max_length=200)
    client_photo = models.ImageField(upload_to="testimonials/", blank=True)
    
    # Testimonial content
    review = models.TextField()
    rating = models.IntegerField(default=5, choices=[(i, str(i)) for i in range(1, 6)])
    
    # Social proof
    project_link = models.CharField(max_length=200, blank=True, help_text="Link to associated project")
    
    # Admin
    is_featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-is_featured', '-order', '-created_at']
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"
    
    def __str__(self):
        return f"{self.client_name} - {self.client_company}"
