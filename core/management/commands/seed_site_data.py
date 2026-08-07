from io import BytesIO

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from PIL import Image, ImageDraw, ImageFont

from projects.models import Project, ProjectCategory
from services.models import Service, ServiceCategory


def _placeholder_image(title: str, color: tuple[int, int, int]) -> ContentFile:
    image = Image.new("RGB", (1200, 800), color)
    draw = ImageDraw.Draw(image)
    text = title[:40]
    draw.text((60, 360), text, fill=(255, 255, 255))
    buffer = BytesIO()
    image.save(buffer, format="JPEG", quality=85)
    return ContentFile(buffer.getvalue(), name=f"{slugify(title) or 'image'}.jpg")


class Command(BaseCommand):
    help = "Seed project/service categories and sample content if the database is empty."

    def handle(self, *args, **options):
        self._seed_categories()
        self._seed_services()
        self._seed_projects()
        self.stdout.write(self.style.SUCCESS("Site seed complete."))

    def _seed_categories(self):
        project_categories = [
            ("Handrail", "handrail", 1),
            ("LTZ Windows and Doors", "ltz-windows-and-doors", 2),
            ("Stainless Steel Handrail", "stainless-steel-handrail", 3),
            ("Frameless and Glass Partition", "frameless-and-glass-partition", 4),
            ("ACP Cladding", "acp-cladding", 5),
            ("Curtain Wall Facade", "curtain-wall-facade", 6),
        ]
        for name, slug, order in project_categories:
            ProjectCategory.objects.get_or_create(
                slug=slug,
                defaults={"name": name, "order": order},
            )

        service_categories = [
            ("Aluminum Systems", 1),
            ("Glass Solutions", 2),
            ("Steel Works", 3),
        ]
        for name, order in service_categories:
            ServiceCategory.objects.get_or_create(
                name=name,
                defaults={"order": order, "description": f"{name} for commercial and residential projects."},
            )

    def _seed_services(self):
        if Service.objects.exists():
            self.stdout.write("Services already exist — skipping sample services.")
            return

        aluminum = ServiceCategory.objects.filter(name="Aluminum Systems").first()
        glass = ServiceCategory.objects.filter(name="Glass Solutions").first()
        steel = ServiceCategory.objects.filter(name="Steel Works").first()

        samples = [
            {
                "title": "Curtain Wall Facade",
                "category": aluminum,
                "short_description": "Modern curtain wall systems for towers and commercial buildings.",
                "description": "Design, fabrication, and installation of premium aluminum curtain wall facade systems.",
                "icon": "fas fa-building",
                "features": "Custom aluminum profiles\nWeather-resistant sealing\nEnergy-efficient glazing\nOn-site installation",
                "color": (10, 46, 111),
            },
            {
                "title": "LTZ Windows and Doors",
                "category": aluminum,
                "short_description": "High-performance aluminum windows and doors for any project scale.",
                "description": "Premium LTZ aluminum windows and doors with durable finishes and smooth operation.",
                "icon": "fas fa-door-open",
                "features": "Thermal break profiles\nSecure locking systems\nCustom sizes\nLow maintenance",
                "color": (23, 78, 166),
            },
            {
                "title": "Frameless Glass Partition",
                "category": glass,
                "short_description": "Elegant frameless glass partitions for offices and interiors.",
                "description": "Frameless glass partition systems that maximize light and create modern workspaces.",
                "icon": "fas fa-border-none",
                "features": "Tempered safety glass\nMinimal hardware\nAcoustic options\nFast installation",
                "color": (45, 156, 219),
            },
            {
                "title": "Stainless Steel Handrail",
                "category": steel,
                "short_description": "Durable stainless steel handrails for stairs, balconies, and public spaces.",
                "description": "Custom stainless steel handrail fabrication with polished or brushed finishes.",
                "icon": "fas fa-grip-lines-vertical",
                "features": "Corrosion resistant\nCustom bends and joints\nIndoor and outdoor use\nSafety compliant",
                "color": (6, 29, 77),
            },
        ]

        for index, sample in enumerate(samples, start=1):
            image_file = _placeholder_image(sample["title"], sample["color"])
            Service.objects.create(
                category=sample["category"],
                title=sample["title"],
                slug=slugify(sample["title"]),
                description=sample["description"],
                short_description=sample["short_description"],
                image=image_file,
                icon=sample["icon"],
                features=sample["features"],
                applications="Commercial buildings\nResidential projects\nHotels and offices",
                benefits="Premium finish\nLong service life\nExpert installation",
                order=index,
                is_featured=True,
                is_active=True,
            )

        self.stdout.write(self.style.SUCCESS(f"Created {len(samples)} sample services."))

    def _seed_projects(self):
        if Project.objects.exists():
            self.stdout.write("Projects already exist — skipping sample projects.")
            return

        category = ProjectCategory.objects.filter(slug="curtain-wall-facade").first()
        if category is None:
            self.stdout.write("No project categories found — skipping sample projects.")
            return

        samples = [
            {
                "title": "Bole Commercial Tower Facade",
                "location": "Bole, Addis Ababa",
                "client": "Private Developer",
                "year": 2025,
                "materials_used": "Aluminum curtain wall profiles\nDouble glazed units\nStructural silicone",
                "color": (10, 46, 111),
            },
            {
                "title": "Airport Road Office Partition",
                "location": "Bole Sub-City, Addis Ababa",
                "client": "Corporate Client",
                "year": 2024,
                "materials_used": "Tempered glass\nStainless fittings\nAluminum channels",
                "color": (23, 78, 166),
            },
            {
                "title": "Residential Balcony Handrail",
                "location": "CMC, Addis Ababa",
                "client": "Residential Client",
                "year": 2024,
                "materials_used": "Stainless steel\nPowder-coated posts\nSafety glass panels",
                "color": (45, 156, 219),
            },
        ]

        for index, sample in enumerate(samples, start=1):
            featured = _placeholder_image(f"{sample['title']} featured", sample["color"])
            after = _placeholder_image(f"{sample['title']} after", sample["color"])
            Project.objects.create(
                category=category,
                title=sample["title"],
                slug=slugify(sample["title"]),
                description=f"Completed {sample['title'].lower()} delivered with premium materials and expert installation.",
                featured_image=featured,
                after_image=after,
                location=sample["location"],
                client=sample["client"],
                year=sample["year"],
                duration="3 months",
                materials_used=sample["materials_used"],
                challenges="Tight schedule and complex facade geometry.",
                solutions="Prefabricated modules and coordinated site installation.",
                results="High-quality finish with improved building appearance and performance.",
                client_feedback="Professional team and excellent workmanship.",
                client_rating=5,
                is_featured=True,
                is_active=True,
                order=index,
            )

        self.stdout.write(self.style.SUCCESS(f"Created {len(samples)} sample projects."))
