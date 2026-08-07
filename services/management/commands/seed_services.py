from django.core.management.base import BaseCommand
from services.models import ServiceCategory, Service


class Command(BaseCommand):
    help = 'Seed services and service categories'

    def handle(self, *args, **kwargs):

        # ── Create categories ──────────────────────────────────
        cat_aluminum, _ = ServiceCategory.objects.get_or_create(
            name='Aluminum Works',
            defaults={'description': 'Premium aluminum fabrication and installation', 'order': 1}
        )
        cat_glass, _ = ServiceCategory.objects.get_or_create(
            name='Glass Works',
            defaults={'description': 'Frameless glass and partition systems', 'order': 2}
        )
        cat_steel, _ = ServiceCategory.objects.get_or_create(
            name='Stainless Steel Works',
            defaults={'description': 'Premium stainless steel fabrication', 'order': 3}
        )
        cat_facade, _ = ServiceCategory.objects.get_or_create(
            name='Facade Systems',
            defaults={'description': 'Curtain wall and ACP cladding systems', 'order': 4}
        )

        self.stdout.write('Categories created.')

        # ── Services ───────────────────────────────────────────
        services = [
            # ── Aluminum Works ──
            {
                'title': 'Handrail',
                'slug': 'handrail',
                'category': cat_aluminum,
                'short_description': 'Elegant and durable handrail systems for staircases, balconies, and walkways.',
                'description': 'We design and install high-quality handrail systems for both interior and exterior use. Our handrails combine safety with modern aesthetics, available in various finishes.',
                'icon': 'bi bi-ladder',
                'features': 'Custom design and fabrication\nPowder-coated and anodized finishes\nResidential and commercial applications\nSafety-compliant installation\nLow maintenance materials',
                'applications': 'Staircases\nBalconies\nRamps and walkways\nCommercial buildings',
                'benefits': 'Enhances safety and aesthetics\nLong-lasting durability\nCustomizable to any design',
                'order': 1,
            },
            {
                'title': 'LTZ Windows and Doors',
                'slug': 'ltz-windows-doors',
                'category': cat_aluminum,
                'short_description': 'High-performance aluminum windows and doors combining energy efficiency with modern design.',
                'description': 'Our LTZ windows and doors are engineered for maximum performance, offering superior insulation, security, and aesthetic value for residential and commercial projects.',
                'icon': 'bi bi-door-open',
                'features': 'Custom sizing and profiles\nDouble and triple glazing options\nThermal break technology\nMulti-point locking systems\nWide range of finishes',
                'applications': 'Residential homes\nOffice buildings\nHotels and hospitality\nRetail spaces',
                'benefits': 'Improved energy efficiency\nEnhanced security\nNoise reduction\nLow maintenance',
                'order': 2,
            },

            # ── Glass Works ──
            {
                'title': 'Frameless and Glass Partition',
                'slug': 'frameless-glass-partition',
                'category': cat_glass,
                'short_description': 'Elegant frameless glass partitions creating open, light-filled spaces without sacrificing privacy.',
                'description': 'Transform your interior spaces with our frameless and semi-frameless glass partition systems using toughened safety glass.',
                'icon': 'bi bi-columns-gap',
                'features': 'Toughened safety glass\nFrameless and minimal frame options\nAcoustic insulation glass available\nSliding and hinged door systems\nFrost and smart glass options',
                'applications': 'Office spaces\nConference rooms\nRetail showrooms\nResidential interiors',
                'benefits': 'Maximizes natural light\nCreates modern open spaces\nAcoustic privacy options\nEasy to clean and maintain',
                'order': 3,
            },

            # ── Stainless Steel Works ──
            {
                'title': 'Stainless Steel Handrail',
                'slug': 'stainless-steel-handrail',
                'category': cat_steel,
                'short_description': 'Premium stainless steel handrail systems delivering a sleek, modern look with exceptional strength.',
                'description': 'Our stainless steel handrail systems offer a perfect blend of elegance and durability, fabricated from high-grade stainless steel.',
                'icon': 'bi bi-gem',
                'features': 'Grade 304 and 316 stainless steel\nPolished and brushed finishes\nCustom post spacing and heights\nGlass panel integration\nCorrosion resistant\nPrecision TIG welding',
                'applications': 'Luxury residences\nHotels and resorts\nShopping centers\nOffice lobbies\nOutdoor terraces',
                'benefits': 'Rust and corrosion resistant\nPremium appearance\nMinimal maintenance\nHigh strength and durability',
                'order': 4,
            },

            # ── Facade Systems ──
            {
                'title': 'ACP Cladding',
                'slug': 'acp-cladding',
                'category': cat_facade,
                'short_description': 'Aluminum Composite Panel cladding for stunning building facades with superior weather protection.',
                'description': 'ACP cladding dramatically transforms building facades providing excellent weather resistance, fire protection, and insulation.',
                'icon': 'bi bi-bricks',
                'features': 'PVDF and polyester coatings\nFire-resistant FR core panels\nWide color and texture range\nLightweight yet rigid\nWeather and UV resistant',
                'applications': 'Commercial building facades\nShopping malls\nHospitals and schools\nHotel exteriors',
                'benefits': 'Transforms building appearance\nExcellent weather protection\nLow maintenance exterior\nCost-effective facade solution',
                'order': 5,
            },
            {
                'title': 'Curtain Wall Facade',
                'slug': 'curtain-wall-facade',
                'category': cat_facade,
                'short_description': 'High-performance curtain wall systems creating iconic glass facades for modern commercial buildings.',
                'description': 'Our curtain wall facade systems deliver stunning all-glass building exteriors that combine architectural beauty with superior structural performance.',
                'icon': 'bi bi-building',
                'features': 'Unitized and stick-built systems\nHigh-performance thermal insulation\nStructural silicone glazing\nCustom aluminum profiles\nWind and water tested',
                'applications': 'High-rise office towers\nHotel buildings\nGovernment buildings\nCommercial complexes',
                'benefits': 'Iconic architectural appearance\nSuperior thermal performance\nStructural integrity\nMaximum natural light',
                'order': 6,
            },
        ]

        for data in services:
            service, created = Service.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'category': data['category'],
                    'short_description': data['short_description'],
                    'description': data['description'],
                    'icon': data['icon'],
                    'features': data['features'],
                    'applications': data.get('applications', ''),
                    'benefits': data.get('benefits', ''),
                    'order': data['order'],
                    'is_active': True,
                    'is_featured': True,
                }
            )
            status = 'Created' if created else 'Updated'
            self.stdout.write(f'  {status}: {service.title} [{service.category.name}]')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {Service.objects.count()} services across {ServiceCategory.objects.count()} categories.'
        ))
