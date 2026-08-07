from django.core.management.base import BaseCommand
from services.models import ServiceCategory, Service


class Command(BaseCommand):
    help = 'Seed services and service categories'

    def handle(self, *args, **kwargs):
        # Create category
        category, _ = ServiceCategory.objects.get_or_create(
            name='Aluminum & Glass Works',
            defaults={'description': 'Premium aluminum and glass solutions', 'order': 1}
        )
        self.stdout.write(f'Category: {category.name}')

        services = [
            {
                'title': 'Handrail',
                'slug': 'handrail',
                'short_description': 'Elegant and durable handrail systems for staircases, balconies, and walkways.',
                'description': 'We design and install high-quality handrail systems for both interior and exterior use. Our handrails combine safety with modern aesthetics.',
                'icon': 'bi bi-ladder',
                'features': 'Custom design and fabrication\nPowder-coated and anodized finishes\nResidential and commercial applications\nSafety-compliant installation',
                'order': 1,
            },
            {
                'title': 'LTZ Windows and Doors',
                'slug': 'ltz-windows-doors',
                'short_description': 'High-performance aluminum windows and doors combining energy efficiency with modern design.',
                'description': 'Our LTZ windows and doors are engineered for maximum performance, offering superior insulation, security, and aesthetic value.',
                'icon': 'bi bi-door-open',
                'features': 'Custom sizing and profiles\nDouble and triple glazing options\nThermal break technology\nMulti-point locking systems',
                'order': 2,
            },
            {
                'title': 'Stainless Steel Handrail',
                'slug': 'stainless-steel-handrail',
                'short_description': 'Premium stainless steel handrail systems delivering a sleek, modern look with exceptional strength.',
                'description': 'Our stainless steel handrail systems offer a perfect blend of elegance and durability.',
                'icon': 'bi bi-gem',
                'features': 'Grade 304 and 316 stainless steel\nPolished and brushed finishes\nCorrosion resistant\nPrecision TIG welding',
                'order': 3,
            },
            {
                'title': 'Frameless and Glass Partition',
                'slug': 'frameless-glass-partition',
                'short_description': 'Elegant frameless glass partitions creating open, light-filled spaces without sacrificing privacy.',
                'description': 'Transform your interior spaces with our frameless and semi-frameless glass partition systems.',
                'icon': 'bi bi-columns-gap',
                'features': 'Toughened safety glass\nFrameless and minimal frame options\nAcoustic insulation glass available\nSliding and hinged door systems',
                'order': 4,
            },
            {
                'title': 'ACP Cladding',
                'slug': 'acp-cladding',
                'short_description': 'Aluminum Composite Panel cladding for stunning building facades with superior weather protection.',
                'description': 'ACP cladding dramatically transforms building facades while providing excellent weather resistance.',
                'icon': 'bi bi-bricks',
                'features': 'PVDF and polyester coatings\nFire-resistant FR core panels\nWide color and texture range\nLightweight yet rigid',
                'order': 5,
            },
            {
                'title': 'Curtain Wall Facade',
                'slug': 'curtain-wall-facade',
                'short_description': 'High-performance curtain wall systems creating iconic glass facades for modern commercial buildings.',
                'description': 'Our curtain wall facade systems deliver stunning all-glass building exteriors with superior structural performance.',
                'icon': 'bi bi-building',
                'features': 'Unitized and stick-built systems\nHigh-performance thermal insulation\nStructural silicone glazing\nWind and water tested',
                'order': 6,
            },
        ]

        for data in services:
            service, created = Service.objects.get_or_create(
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'category': category,
                    'short_description': data['short_description'],
                    'description': data['description'],
                    'icon': data['icon'],
                    'features': data['features'],
                    'order': data['order'],
                    'is_active': True,
                    'is_featured': True,
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'{status}: {service.title}')

        self.stdout.write(self.style.SUCCESS(f'\nDone! Total services: {Service.objects.count()}'))
