from django.core.management.base import BaseCommand
from django.utils.text import slugify
from projects.models import ProjectCategory, Project


class Command(BaseCommand):
    help = 'Seed project categories and projects with static images'

    def handle(self, *args, **kwargs):

        # ── Categories ─────────────────────────────────────────
        categories = [
            {'name': 'Handrail',                     'slug': 'handrail',                    'icon': 'bi bi-ladder',     'order': 1},
            {'name': 'LTZ Windows and Doors',         'slug': 'ltz-windows-doors',           'icon': 'bi bi-door-open',  'order': 2},
            {'name': 'Stainless Steel Handrail',      'slug': 'stainless-steel-handrail',    'icon': 'bi bi-gem',        'order': 3},
            {'name': 'Frameless and Glass Partition', 'slug': 'frameless-glass-partition',   'icon': 'bi bi-columns-gap','order': 4},
            {'name': 'ACP Cladding',                  'slug': 'acp-cladding',                'icon': 'bi bi-bricks',     'order': 5},
            {'name': 'Curtain Wall Facade',           'slug': 'curtain-wall-facade',         'icon': 'bi bi-building',   'order': 6},
        ]

        cats = {}
        for c in categories:
            obj, _ = ProjectCategory.objects.get_or_create(
                slug=c['slug'],
                defaults={'name': c['name'], 'icon': c['icon'], 'order': c['order']}
            )
            cats[c['slug']] = obj

        self.stdout.write('Categories ready.')

        # ── Projects ───────────────────────────────────────────
        projects = [
            {
                'slug': 'handrail-project-1',
                'title': 'Handrail Project',
                'category': cats['handrail'],
                'description': 'High-quality aluminum handrail installation for a residential and commercial building in Addis Ababa.',
                'location': 'Addis Ababa, Ethiopia',
                'client': 'Michael Aluminum and Glass',
                'year': 2025,
                'materials_used': 'Aluminum',
                'static_featured': 'images/Category 1 Handrail/photo_5979042982746853370_y.jpg',
                'static_after':    'images/Category 1 Handrail/photo_5979042982746853352_y.jpg',
                'static_before':   'images/Category 1 Handrail/photo_5979042982746853353_x.jpg',
            },
            {
                'slug': 'ltz-windows-and-doors-project-1',
                'title': 'LTZ Windows and Doors Project',
                'category': cats['ltz-windows-doors'],
                'description': 'Premium LTZ aluminum window and door installation for a modern commercial building.',
                'location': 'Addis Ababa, Ethiopia',
                'client': 'Michael Aluminum and Glass',
                'year': 2025,
                'materials_used': 'Aluminum',
                'static_featured': 'images/category 2 LTZ windows and doors/photo_5979042982746853392_y.jpg',
                'static_after':    'images/category 2 LTZ windows and doors/photo_5979042982746853381_y.jpg',
                'static_before':   '',
            },
            {
                'slug': 'stainless-steel-handrail-project-1',
                'title': 'Stainless Steel Handrail Project',
                'category': cats['stainless-steel-handrail'],
                'description': 'Premium stainless steel handrail system for a luxury residential building.',
                'location': 'Addis Ababa, Ethiopia',
                'client': 'Michael Aluminum and Glass',
                'year': 2025,
                'materials_used': 'Stainless Steel Grade 304',
                'static_featured': 'images/Category 3 Stainless Steal Handrail/photo_5979042982746853405_y.jpg',
                'static_after':    'images/Category 3 Stainless Steal Handrail/photo_5979042982746853399_y.jpg',
                'static_before':   '',
            },
            {
                'slug': 'frameless-and-glass-partition-project-1',
                'title': 'Frameless and Glass Partition Project',
                'category': cats['frameless-glass-partition'],
                'description': 'Modern frameless glass partition system for an office building interior.',
                'location': 'Addis Ababa, Ethiopia',
                'client': 'Michael Aluminum and Glass',
                'year': 2025,
                'materials_used': 'Tempered Glass',
                'static_featured': 'images/Category 4 Frameless and Glass Partition/photo_5979042982746853413_y.jpg',
                'static_after':    'images/Category 4 Frameless and Glass Partition/photo_5979042982746853410_y.jpg',
                'static_before':   'images/Category 4 Frameless and Glass Partition/photo_5979042982746853415_x.jpg',
            },
            {
                'slug': 'acp-cladding-project-1',
                'title': 'ACP Cladding Project',
                'category': cats['acp-cladding'],
                'description': 'Aluminum composite panel cladding for a modern commercial building facade.',
                'location': 'Addis Ababa, Ethiopia',
                'client': 'Michael Aluminum and Glass',
                'year': 2025,
                'materials_used': 'Aluminum Composite Panel',
                'static_featured': 'images/Category 5 ACP Cladding/photo_5979042982746853418_y.jpg',
                'static_after':    'images/Category 5 ACP Cladding/photo_5979042982746853418_y.jpg',
                'static_before':   'images/Category 5 ACP Cladding/photo_5979042982746853419_x.jpg',
            },
            {
                'slug': 'curtain-wall-facade-project-1',
                'title': 'Curtain Wall Facade Project',
                'category': cats['curtain-wall-facade'],
                'description': 'High-performance curtain wall facade system for a high-rise commercial building.',
                'location': 'Addis Ababa, Ethiopia',
                'client': 'Michael Aluminum and Glass',
                'year': 2025,
                'materials_used': 'Aluminum, Tempered Glass',
                'static_featured': 'images/Category 6 Curtain Wall Facade/photo_5979042982746853452_y.jpg',
                'static_after':    'images/Category 6 Curtain Wall Facade/photo_5979042982746853448_y.jpg',
                'static_before':   'images/Category 6 Curtain Wall Facade/photo_5979042982746853447_x.jpg',
            },
        ]

        for data in projects:
            project, created = Project.objects.update_or_create(
                slug=data['slug'],
                defaults={
                    'title': data['title'],
                    'category': data['category'],
                    'description': data['description'],
                    'location': data['location'],
                    'client': data['client'],
                    'year': data['year'],
                    'materials_used': data['materials_used'],
                    'static_featured': data['static_featured'],
                    'static_after':    data['static_after'],
                    'static_before':   data['static_before'],
                    'featured_image':  None,
                    'before_image':    None,
                    'after_image':     None,
                    'is_active': True,
                    'is_featured': True,
                }
            )
            self.stdout.write(f'  {"Created" if created else "Updated"}: {project.title} [{project.category.name}]')

        self.stdout.write(self.style.SUCCESS(
            f'\nDone! {Project.objects.count()} projects across {ProjectCategory.objects.count()} categories.'
        ))
