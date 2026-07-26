# Michael Aluminum and Glass Technology — Site Guide

---

## Local Development

```bash
cd c:\Users\Get_TechAcad\Documents\PROJECTS\Michael
venv\Scripts\activate
python manage.py runserver
```
Open: http://127.0.0.1:8000
Admin: http://127.0.0.1:8000/admin/

---

## Deploy to Render — Step by Step

### Step 1: Push to GitHub

1. Create a new repo on https://github.com/new  
   Name it: `michael-aluminum`

2. In your terminal:
```bash
git init
git add .
git commit -m "Initial deployment"
git branch -M main
git remote add origin https://github.com/getachewzemichael/michael-aluminum.git
git push -u origin main
```

> **Before pushing**, make sure `.env` is NOT committed (it's in `.gitignore` already)

---

### Step 2: Create a PostgreSQL Database on Render

1. Go to https://dashboard.render.com
2. Click **New → PostgreSQL**
3. Name: `michael-aluminum-db`
4. Plan: **Free**
5. Click **Create Database**
6. Copy the **Internal Database URL** — you will need it

---

### Step 3: Create a Web Service on Render

1. Click **New → Web Service**
2. Connect your GitHub repo: `michael-aluminum`
3. Fill in:

| Field | Value |
|-------|-------|
| Name | `michael-aluminum` |
| Runtime | `Python 3` |
| Build Command | `./build.sh` |
| Start Command | `gunicorn MichaelAluminum.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 120` |
| Plan | Free |

---

### Step 4: Set Environment Variables on Render

In the web service → **Environment** tab, add:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | Click **Generate** |
| `DEBUG` | `false` |
| `ALLOWED_HOSTS` | `.onrender.com` |
| `DATABASE_URL` | Paste the Internal Database URL from Step 2 |
| `CSRF_TRUSTED_ORIGINS` | `https://michael-aluminum.onrender.com` |
| `CORS_ALLOWED_ORIGINS` | `https://michael-aluminum.onrender.com` |
| `EMAIL_BACKEND` | `django.core.mail.backends.smtp.EmailBackend` |
| `EMAIL_HOST_USER` | `michaeltadessemiki@gmail.com` |
| `EMAIL_HOST_PASSWORD` | Your Gmail App Password |

> For Gmail App Password: go to https://myaccount.google.com/apppasswords

---

### Step 5: Deploy

1. Click **Create Web Service**
2. Render will run `build.sh` automatically:
   - Installs requirements
   - Runs `collectstatic`
   - Runs `migrate`
3. Wait 3–5 minutes for first deploy
4. Your site will be live at: `https://michael-aluminum.onrender.com`

---

### Step 6: Create Admin Superuser

After deploy, go to Render dashboard → your web service → **Shell** tab:

```bash
python manage.py createsuperuser
```

Enter username, email, and password.

---

## Site Pages

| Page | URL |
|------|-----|
| Home | `/` |
| About | `/about/` |
| Services | `/services/` |
| Projects | `/projects/` |
| Gallery | `/gallery/` |
| Blog | `/blog/` |
| Contact | `/contact/` |
| Quote | `/quotations/request/` |
| Admin | `/admin/` |
| Terms | `/terms/` |
| Privacy | `/privacy/` |
| Dashboard | `/dashboard/` (staff only) |

---

## Project Categories (in DB)

1. Handrail
2. LTZ Windows and Doors
3. Stainless Steel Handrail
4. Frameless and Glass Partition
5. ACP Cladding
6. Curtain Wall Facade

---

## Important Notes

- **Media files** (uploaded images) are NOT persistent on Render's free plan.  
  For production media storage, use **Cloudinary** — add credentials to env vars.
- Free Render services **spin down** after 15 minutes of inactivity — first request takes ~30s.
- Upgrade to a paid plan to keep the service always active.

---

## Developer

**Getachew Zemicheal** — GitHub: [getachewzemichael](https://github.com/getachewzemichael)  
Last Updated: July 2026
