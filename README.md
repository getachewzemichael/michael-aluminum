# Michael Aluminum and Glass Technology - Corporate Website

Building the Future with Premium Aluminum & Glass Solutions

## Project Overview

A corporate website for Michael Aluminum and Glass Technology, built with Django 5.0, Bootstrap 5.3, and modern UI/UX principles.

### Features
- Responsive mobile-first design
- Glassmorphism UI with smooth animations
- Dark/light theme toggle
- Multi-language support (English, Amharic, Tigrinya)
- Project portfolio with category filtering
- Blog system
- Quotation request system
- Career portal
- Contact form with email notifications
- REST API for external integrations

## Tech Stack

- **Backend** — Django 5.0, Django REST Framework
- **Database** — SQLite (development), PostgreSQL (production)
- **Frontend** — Bootstrap 5.3, Custom CSS, AOS, GSAP, Swiper.js, LightGallery
- **Static Files** — WhiteNoise
- **Web Server** — Gunicorn + Nginx
- **Container** — Docker

## Installation

```bash
# Clone the repository
git clone https://github.com/getachewzemichael/michael-aluminum.git
cd michael-aluminum

# Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Create .env file (see .env.example)
# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

Visit http://localhost:8000

## Environment Variables

Copy `.env.example` to `.env` and fill in:

```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

## Project Structure

```
michael-aluminum/
├── MichaelAluminum/    # Django settings and URL config
├── core/               # Home and About pages
├── services/           # Services management
├── projects/           # Portfolio (6 categories)
├── gallery/            # Image/video gallery
├── blog/               # Blog system
├── testimonials/       # Client testimonials
├── careers/            # Job listings
├── contact/            # Contact form
├── quotations/         # Quote requests
├── dashboard/          # Admin dashboard
├── api/                # REST API
├── templates/          # HTML templates
├── static/             # CSS, JS, images
└── media/              # Uploaded files
```

## Project Categories

1. Handrail
2. LTZ Windows and Doors
3. Stainless Steel Handrail
4. Frameless and Glass Partition
5. ACP Cladding
6. Curtain Wall Facade

## Admin

Access at `/admin/` to manage projects, services, blog posts, quotations, and more.

## Deployment

### Docker
```bash
docker build -t michael-aluminum .
docker run -p 8000:8000 michael-aluminum
```

### Production Environment Variables
```
DEBUG=False
SECRET_KEY=strong-secret-key
ALLOWED_HOSTS=yourdomain.com
DATABASE_URL=postgresql://user:pass@host/db
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

## Contact

**Michael Aluminum and Glass Technology**
- Email: michaeltadessemiki@gmail.com
- Phone: +251-962-294-612 / +251-988-994-268
- Address: Bole Sub-City, Addis Ababa, Ethiopia
- TikTok: [@michaelaluminum](https://www.tiktok.com/@michaelaluminum)

## Developer

**Getachew Zemicheal** — [GitHub: getachewzemichael](https://github.com/getachewzemichael)

---

Last Updated: July 22, 2026 | Version: 1.0.0
