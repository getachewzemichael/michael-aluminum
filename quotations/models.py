from django.db import models


class Quotation(models.Model):
    """Quote requests from customers"""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewing', 'Under Review'),
        ('quoted', 'Quoted'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]
    
    # Personal Information
    full_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    
    # Project Details
    service_needed = models.CharField(max_length=200)
    project_location = models.CharField(max_length=300)
    project_description = models.TextField()
    
    # Budget and Timeline
    budget = models.CharField(max_length=100, blank=True, help_text="e.g., Budget Range")
    expected_completion_date = models.DateField(blank=True, null=True)
    
    # Files
    drawings = models.FileField(upload_to="quotations/drawings/", blank=True)
    additional_files = models.FileField(upload_to="quotations/files/", blank=True)
    
    # Admin
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    notes = models.TextField(blank=True, help_text="Internal notes")
    assigned_to = models.CharField(max_length=200, blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Quotation"
        verbose_name_plural = "Quotations"
    
    def __str__(self):
        return f"Quote from {self.full_name} - {self.status}"


class QuotationResponse(models.Model):
    """Response to quotation requests"""
    quotation = models.OneToOneField(Quotation, on_delete=models.CASCADE, related_name='response')
    
    # Quote details
    quote_number = models.CharField(max_length=50, unique=True)
    quote_amount = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.CharField(max_length=3, default='USD')
    
    # Description
    description = models.TextField()
    scope_of_work = models.TextField()
    terms_conditions = models.TextField(blank=True)
    
    # Timeline
    estimated_duration = models.CharField(max_length=100)
    delivery_date = models.DateField()
    
    # File
    quote_document = models.FileField(upload_to="quotations/responses/")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Quotation Response"
        verbose_name_plural = "Quotation Responses"
    
    def __str__(self):
        return f"Quote {self.quote_number}"
