from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = 'Seed all site data: company info, testimonials, blog posts'

    def handle(self, *args, **kwargs):
        self.seed_company_info()
        self.seed_testimonials()
        self.seed_blog_posts()
        self.stdout.write(self.style.SUCCESS('All data seeded successfully.'))

    def seed_company_info(self):
        from core.models import CompanyInfo, SiteSettings
        obj, created = CompanyInfo.objects.get_or_create(id=1, defaults={
            'name': 'Michael Aluminum and Glass Technology',
            'tagline': 'Building the Future with Premium Aluminum & Glass Solutions',
            'description': '''Michael Aluminum and Glass Technology is a premier aluminum, glass, and stainless steel fabrication and installation company based in Bole Sub-City, Addis Ababa, Ethiopia. Founded by Michael Tadesse, the company was built on years of hands-on expertise and a deep commitment to delivering world-class architectural solutions across Ethiopia and East Africa.

We specialize in LTZ aluminum windows and doors, curtain wall facade systems, ACP cladding, frameless glass partitions, stainless steel handrails, and custom aluminum handrail systems. Every project is executed with precision, professionalism, and an unwavering dedication to quality.

ሚካኤል የአሉሚኒየምና የመስተዋት ስራ — quality፣ integrity እና craftsmanship ያለን foundation ነው።''',
            'email': 'michaeltadessemiki@gmail.com',
            'phone': '+251-962-294-612',
            'whatsapp': '+251962294612',
            'telegram': '@michaelalumin',
            'facebook': '#',
            'instagram': '#',
            'linkedin': '#',
            'youtube': '#',
            'tiktok': 'https://www.tiktok.com/@michaelaluminum',
            'address': 'Bole Sub-City, Near Bole International Airport',
            'city': 'Addis Ababa',
            'country': 'Ethiopia',
            'years_experience': 10,
            'projects_completed': 30,
            'happy_clients': 25,
            'team_members': 10,
            'meta_description': 'Premium aluminum, glass and stainless steel solutions in Addis Ababa, Ethiopia.',
            'meta_keywords': 'aluminum, glass, stainless steel, curtain wall, ACP cladding, handrail, Ethiopia',
        })
        if not created:
            obj.email = 'michaeltadessemiki@gmail.com'
            obj.phone = '+251-962-294-612'
            obj.tiktok = 'https://www.tiktok.com/@michaelaluminum'
            obj.save()
        SiteSettings.objects.get_or_create(id=1, defaults={'enable_dark_mode': True, 'default_language': 'en'})
        self.stdout.write(f'  Company Info: {"Created" if created else "Updated"}')

    def seed_testimonials(self):
        from testimonials.models import Testimonial
        testimonials = [
            {
                'client_name': 'Abebe Kebede',
                'client_company': 'Kebede Real Estate, Addis Ababa',
                'review': 'Michael Aluminum ፕሮጀክታችንን outstanding quality ባለው ሁኔታ deliver አደረጉ — highly professional team ነው። Curtain wall facade ስራው ከምንጠብቀው በላይ ጥሩ ሆነ።',
                'rating': 5,
                'is_active': True,
            },
            {
                'client_name': 'Tigist Haile',
                'client_company': 'Haile Construction PLC, Addis Ababa',
                'review': 'The frameless glass partition installed in our office is exceptional. Professional team, on-time delivery, and the quality is outstanding. We highly recommend Michael Aluminum.',
                'rating': 5,
                'is_active': True,
            },
            {
                'client_name': 'Dawit Mengistu',
                'client_company': 'Mengistu Developers, Addis Ababa',
                'review': 'ACP cladding ስራው ህንፃችንን ሙሉ ለሙሉ ቀይሮታል — the building looks completely transformed. Great craftsmanship and very competitive pricing.',
                'rating': 5,
                'is_active': True,
            },
            {
                'client_name': 'Selamawit Tadesse',
                'client_company': 'Premium Homes Ethiopia',
                'review': 'The stainless steel handrails installed in our luxury residential project are beautiful and very durable. Michael Aluminum delivered exactly what we envisioned.',
                'rating': 5,
                'is_active': True,
            },
            {
                'client_name': 'Yohannes Bekele',
                'client_company': 'Bekele & Associates Architects',
                'review': 'LTZ windows and doors ስራው በጣም ጥሩ ነው — energy efficient, secure, and aesthetically pleasing. ደምበኞቻችን ሁሉ ደስተኞች ናቸው።',
                'rating': 5,
                'is_active': True,
            },
        ]
        for t in testimonials:
            _, created = Testimonial.objects.get_or_create(client_name=t['client_name'], defaults=t)
            self.stdout.write(f'  Testimonial {"Created" if created else "Exists"}: {t["client_name"]}')

    def seed_blog_posts(self):
        from blog.models import BlogPost, BlogCategory
        cat, _ = BlogCategory.objects.get_or_create(
            name='Industry Insights',
            defaults={'slug': 'industry-insights', 'description': 'Aluminum and glass industry insights'}
        )
        posts = [
            {
                'title': 'Why ACP Cladding is the Best Choice for Modern Building Facades',
                'slug': 'why-acp-cladding-best-choice-modern-building-facades',
                'excerpt': 'Discover why ACP cladding is the most popular facade solution for modern commercial buildings in Ethiopia and East Africa.',
                'content': '''Aluminum Composite Panel (ACP) cladding has become the go-to facade solution for modern commercial buildings across Ethiopia. Here is why:

**1. Dramatic Transformation**
ACP cladding can completely transform the appearance of any building. Available in hundreds of colors and finishes. ህንፃዎን ሙሉ ለሙሉ መቀየር ይቻላል።

**2. Superior Weather Protection**
ACP panels with PVDF coatings provide excellent UV resistance and weather protection for decades against Ethiopian weather conditions.

**3. Lightweight Yet Strong**
Unlike traditional brick cladding, ACP panels are lightweight, reducing structural load while maintaining high strength.

**4. Cost-Effective**
ACP cladding offers one of the best value-for-money ratios in facade systems with faster installation.

**5. Low Maintenance**
A simple wash with water keeps it looking new for years.

Contact Michael Aluminum and Glass Technology today for a free consultation on your facade project.''',
                'is_published': True,
                'views_count': 0,
            },
            {
                'title': 'The Benefits of Stainless Steel Handrails for Luxury Buildings',
                'slug': 'benefits-stainless-steel-handrails-luxury-buildings',
                'excerpt': 'Grade 304 and 316 stainless steel handrails — discover why premium buildings choose stainless steel for their handrail systems.',
                'content': '''Stainless steel handrails have become the hallmark of luxury construction in Ethiopia.

**1. Unmatched Durability**
Grade 304 and 316 stainless steel resist corrosion and rust for decades. ዘለቄታዊ ጥራት።

**2. Premium Aesthetic**
The polished or brushed finish adds an unmistakable premium look to any space.

**3. Safety and Strength**
Superior structural strength ensuring safety in both residential and commercial settings.

**4. Versatility**
Can be combined with glass panels or wood inserts to match any architectural style.

**5. Hygienic**
Non-porous and easy to clean — perfect for high-traffic areas.

Contact Michael Aluminum for custom stainless steel handrail fabrication and installation.''',
                'is_published': True,
                'views_count': 0,
            },
            {
                'title': 'How Curtain Wall Facades Are Transforming the Addis Ababa Skyline',
                'slug': 'curtain-wall-facades-transforming-addis-ababa-skyline',
                'excerpt': 'Curtain wall facade systems are changing the Addis Ababa skyline — learn how they bring modern architecture to Ethiopia.',
                'content': '''The Addis Ababa skyline is rapidly evolving and curtain wall facades are at the heart of this transformation.

**What is a Curtain Wall?**
A curtain wall is a non-structural outer covering of a building designed to resist air, water, seismic forces, and wind. በኢትዮጵያ ውስጥ ብዙ ህንፃዎች curtain wall ስርዓት ተጠቅመው ዘመናዊ ሆነዋል።

**1. Maximum Natural Light**
Floor-to-ceiling glass curtain walls flood interiors with natural light, reducing electricity costs.

**2. Superior Thermal Performance**
Modern curtain wall systems incorporate thermal break technology improving energy efficiency.

**3. Iconic Appearance**
Nothing makes a building stand out like a sleek glass facade — synonymous with prestige and modernity.

**4. Structural Integrity**
Engineered to withstand wind loads and seismic forces.

Contact Michael Aluminum and Glass Technology to transform your building project today.''',
                'is_published': True,
                'views_count': 0,
            },
        ]
        for p in posts:
            _, created = BlogPost.objects.get_or_create(
                slug=p['slug'],
                defaults={**p, 'category': cat, 'published_at': timezone.now()}
            )
            self.stdout.write(f'  Blog Post {"Created" if created else "Exists"}: {p["title"][:50]}')
