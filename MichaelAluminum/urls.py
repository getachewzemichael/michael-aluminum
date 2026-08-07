"""
URL configuration for MichaelAluminum project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import Sitemap
from django.http import HttpResponse


# ── Sitemaps ──────────────────────────────────────────────────
from projects.models import Project
from services.models import Service
from blog.models import BlogPost


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'
    protocol = 'https'

    def items(self):
        return ['/', '/about/', '/services/', '/projects/',
                '/gallery/', '/blog/', '/contact/', '/quotations/request/']

    def location(self, item):
        return item


class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Project.objects.filter(is_active=True)

    def location(self, obj):
        return f'/projects/{obj.slug}/'


class ServiceSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Service.objects.filter(is_active=True)

    def location(self, obj):
        return f'/services/{obj.slug}/'


class BlogSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7
    protocol = 'https'

    def items(self):
        return BlogPost.objects.filter(is_published=True)

    def location(self, obj):
        return f'/blog/{obj.slug}/'


sitemaps = {
    'static': StaticViewSitemap,
    'projects': ProjectSitemap,
    'services': ServiceSitemap,
    'blog': BlogSitemap,
}


def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        "Disallow: /api/",
        "",
        f"Sitemap: https://michael-aluminum.onrender.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


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
    path("sitemap.xml", sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", robots_txt),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
