from django.db import models


class Language(models.Model):
    """Available languages"""
    code = models.CharField(max_length=10, unique=True, help_text="e.g., en, am")
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"
    
    def __str__(self):
        return f"{self.name} ({self.code})"


class AboutPageContent(models.Model):
    """About page content in different languages"""
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='about_content')
    title = models.CharField(max_length=200)
    description = models.TextField()
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('language',)
        verbose_name = "About Page Content"
        verbose_name_plural = "About Page Content"
    
    def __str__(self):
        return f"About - {self.language.name}"


class WhyChooseUsContent(models.Model):
    """Why Choose Us content in different languages"""
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='why_choose_us_content')
    item = models.CharField(max_length=300)
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        unique_together = ('language', 'item')
        verbose_name = "Why Choose Us Item"
        verbose_name_plural = "Why Choose Us Items"
    
    def __str__(self):
        return f"{self.item} - {self.language.name}"


class ServiceContent(models.Model):
    """Service content in different languages"""
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='service_content')
    service_name = models.CharField(max_length=100)
    items = models.TextField(help_text="Service items separated by newline")
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        unique_together = ('language', 'service_name')
        verbose_name = "Service Content"
        verbose_name_plural = "Service Content"
    
    def __str__(self):
        return f"{self.service_name} - {self.language.name}"
    
    def get_items_list(self):
        return [item.strip() for item in self.items.split('\n') if item.strip()]


class ProcessContent(models.Model):
    """Our Process content in different languages"""
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='process_content')
    step_name = models.CharField(max_length=100)
    step_description = models.TextField()
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        unique_together = ('language', 'step_name')
        verbose_name = "Process Step"
        verbose_name_plural = "Process Steps"
    
    def __str__(self):
        return f"{self.step_name} - {self.language.name}"


class MaterialsContent(models.Model):
    """Materials content in different languages"""
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='materials_content')
    material_type = models.CharField(max_length=100)
    specifications = models.TextField(help_text="Specifications separated by newline")
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['order']
        unique_together = ('language', 'material_type')
        verbose_name = "Material"
        verbose_name_plural = "Materials"
    
    def __str__(self):
        return f"{self.material_type} - {self.language.name}"
    
    def get_specifications_list(self):
        return [spec.strip() for spec in self.specifications.split('\n') if spec.strip()]


class VisionValuesContent(models.Model):
    """Vision and Values content in different languages"""
    CONTENT_TYPE_CHOICES = [
        ('vision', 'Vision'),
        ('value', 'Value'),
    ]
    
    language = models.ForeignKey(Language, on_delete=models.CASCADE, related_name='vision_values_content')
    content_type = models.CharField(max_length=20, choices=CONTENT_TYPE_CHOICES)
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['content_type', 'order']
        unique_together = ('language', 'content_type', 'title')
        verbose_name = "Vision/Value"
        verbose_name_plural = "Vision/Values"
    
    def __str__(self):
        return f"{self.get_content_type_display()} - {self.title} ({self.language.name})"
