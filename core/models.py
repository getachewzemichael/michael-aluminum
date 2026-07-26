from django.db import models


class CompanyInfo(models.Model):
    """Store company information and settings"""
    name = models.CharField(max_length=255, default="Michael Aluminum and Glass Technology")
    tagline = models.CharField(max_length=500, default="Building the Future with Premium Aluminum & Glass Solutions")
    description = models.TextField()
    
    # Contact Information
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    whatsapp = models.CharField(max_length=20, blank=True)
    telegram = models.CharField(max_length=50, blank=True)
    
    # Social Media
    facebook = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    tiktok = models.URLField(blank=True)
    
    # Address
    address = models.TextField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    # Business Info
    years_experience = models.IntegerField(default=10)
    projects_completed = models.IntegerField(default=500)
    happy_clients = models.IntegerField(default=200)
    team_members = models.IntegerField(default=25)
    
    # Logo and Favicon
    logo = models.ImageField(upload_to="company/", null=True, blank=True)
    favicon = models.ImageField(upload_to="company/", null=True, blank=True)
    
    # Hero Background
    hero_image = models.ImageField(upload_to="hero/", null=True, blank=True)
    
    # SEO
    meta_description = models.CharField(max_length=160)
    meta_keywords = models.CharField(max_length=255)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"
    
    def __str__(self):
        return self.name


class SiteSettings(models.Model):
    """Global site settings"""
    enable_dark_mode = models.BooleanField(default=True)
    enable_newsletter = models.BooleanField(default=True)
    enable_live_chat = models.BooleanField(default=True)
    maintenance_mode = models.BooleanField(default=False)
    
    # Language settings
    default_language = models.CharField(max_length=10, default="en")
    enable_amharic = models.BooleanField(default=True)
    enable_tigrinya = models.BooleanField(default=True)
    
    # Google Analytics
    google_analytics_id = models.CharField(max_length=50, blank=True)
    
    # Cloudinary Settings
    cloudinary_cloud_name = models.CharField(max_length=255, blank=True)
    cloudinary_api_key = models.CharField(max_length=255, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"
    
    def __str__(self):
        return "Site Settings"


class StatisticCard(models.Model):
    """Animated statistics on home page"""
    title = models.CharField(max_length=100)
    value = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    icon = models.CharField(max_length=100, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Statistic Card"
        verbose_name_plural = "Statistic Cards"
    
    def __str__(self):
        return f"{self.value} - {self.title}"


class WhyChooseUsCard(models.Model):
    """Why Choose Us section cards"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Font Awesome icon class")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
        verbose_name = "Why Choose Us Card"
        verbose_name_plural = "Why Choose Us Cards"
    
    def __str__(self):
        return self.title
