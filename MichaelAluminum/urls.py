"""
URL configuration for MichaelAluminum project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls", namespace="core")),
    path("services/", include("services.urls", namespace="services")),
    path("projects/", include("projects.urls", namespace="projects")),
    path("gallery/", include("gallery.urls", namespace="gallery")),
    path("blog/", include("blog.urls", namespace="blog")),
    path("testimonials/", include("testimonials.urls", namespace="testimonials")),
    path("careers/", include("careers.urls", namespace="careers")),
    path("contact/", include("contact.urls", namespace="contact")),
    path("quotations/", include("quotations.urls", namespace="quotations")),
    path("api/", include("api.urls", namespace="api")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
