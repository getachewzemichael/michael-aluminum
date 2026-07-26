from django.db import models


class JobPosition(models.Model):
    """Job positions"""
    
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('closed', 'Closed'),
        ('filled', 'Filled'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    requirements = models.TextField(help_text="Requirements separated by newline")
    responsibilities = models.TextField(help_text="Responsibilities separated by newline")
    
    # Position Details
    department = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    employment_type = models.CharField(max_length=50, choices=[
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('internship', 'Internship'),
    ])
    salary_range = models.CharField(max_length=100, blank=True)
    
    # Benefits
    benefits = models.TextField(help_text="Benefits separated by newline", blank=True)
    
    # Admin
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    is_featured = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    closing_date = models.DateField(null=True, blank=True)
    
    class Meta:
        ordering = ['-posted_date']
        verbose_name = "Job Position"
        verbose_name_plural = "Job Positions"
    
    def __str__(self):
        return self.title


class JobApplication(models.Model):
    """Job applications"""
    
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('reviewing', 'Under Review'),
        ('shortlisted', 'Shortlisted'),
        ('interview', 'Interview Scheduled'),
        ('rejected', 'Rejected'),
        ('accepted', 'Accepted'),
    ]
    
    job_position = models.ForeignKey(JobPosition, on_delete=models.CASCADE, related_name='applications')
    
    # Applicant Information
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Application
    cover_letter = models.TextField()
    cv = models.FileField(upload_to="careers/cv/")
    portfolio_link = models.URLField(blank=True)
    linkedin_profile = models.URLField(blank=True)
    
    # Admin
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    notes = models.TextField(blank=True)
    
    applied_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-applied_at']
        verbose_name = "Job Application"
        verbose_name_plural = "Job Applications"
    
    def __str__(self):
        return f"{self.full_name} - {self.job_position.title}"
