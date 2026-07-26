/**
 * Michael Aluminum and Glass Technology
 * main.js — Optimized for fast load, no scroll lag
 */

// ── Wait for all deferred scripts to be ready ──────────────────
document.addEventListener('DOMContentLoaded', function () {

    // ── 1. THEME (runs immediately — no delay) ──────────────────
    const html = document.documentElement;
    const themeToggle = document.getElementById('theme-toggle');
    const saved = localStorage.getItem('theme') || 'light';
    html.setAttribute('data-theme', saved);
    setThemeIcon(saved);

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            const t = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
            html.setAttribute('data-theme', t);
            localStorage.setItem('theme', t);
            setThemeIcon(t);
        });
    }

    function setThemeIcon(t) {
        const icon = themeToggle && themeToggle.querySelector('i');
        if (icon) icon.className = t === 'light' ? 'bi bi-moon' : 'bi bi-sun';
    }

    // ── 2. NAVBAR scroll shadow (passive + rAF throttled) ───────
    const navbar = document.querySelector('.navbar');
    let navTick = false;
    if (navbar) {
        window.addEventListener('scroll', function () {
            if (!navTick) {
                requestAnimationFrame(function () {
                    navbar.classList.toggle('scrolled', window.scrollY > 50);
                    navTick = false;
                });
                navTick = true;
            }
        }, { passive: true });
    }

    // ── 3. BACK TO TOP (passive scroll) ─────────────────────────
    const btt = document.getElementById('back-to-top');
    let bttTick = false;
    if (btt) {
        window.addEventListener('scroll', function () {
            if (!bttTick) {
                requestAnimationFrame(function () {
                    btt.style.display = window.pageYOffset > 300 ? 'flex' : 'none';
                    bttTick = false;
                });
                bttTick = true;
            }
        }, { passive: true });
        btt.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
    }

    // ── 4. STAT COUNTER (IntersectionObserver — zero scroll cost)
    const statEls = document.querySelectorAll('.stat-number, .ab-stat__number');
    if (statEls.length) {
        const cObs = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                const el = entry.target;
                const raw = el.textContent.replace(/[^0-9]/g, '');
                const target = parseInt(raw, 10);
                if (!target) return;
                const suffix = el.textContent.includes('%') ? '%' : '+';
                let count = 0;
                const step = Math.ceil(target / 40);
                const t = setInterval(function () {
                    count = Math.min(count + step, target);
                    el.textContent = count + suffix;
                    if (count >= target) clearInterval(t);
                }, 25);
                cObs.unobserve(el);
            });
        }, { threshold: 0.6 });
        statEls.forEach(el => cObs.observe(el));
    }

    // ── 5. FORM VALIDATION ──────────────────────────────────────
    document.querySelectorAll('form.needs-validation').forEach(function (form) {
        form.addEventListener('submit', function (e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // ── 6. NAVBAR — close on mobile link click ──────────────────
    const navCollapse = document.querySelector('.navbar-collapse');
    if (navCollapse) {
        navCollapse.querySelectorAll('a.nav-link').forEach(function (link) {
            link.addEventListener('click', function () {
                if (window.innerWidth < 992 && navCollapse.classList.contains('show')) {
                    bootstrap.Collapse.getInstance(navCollapse)?.hide();
                }
            });
        });
    }

    // ── 7. FILTER (projects / gallery) ──────────────────────────
    document.querySelectorAll('[data-filter]').forEach(function (btn) {
        btn.addEventListener('click', function () {
            const cat = this.getAttribute('data-filter');
            document.querySelectorAll('[data-filter]').forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            document.querySelectorAll('[data-category]').forEach(function (item) {
                const show = cat === 'all' || item.getAttribute('data-category') === cat;
                item.style.display = show ? '' : 'none';
            });
        });
    });

    // ── 8. HERO — ensure visible immediately ────────────────────
    const heroH1 = document.querySelector('.hero h1');
    if (heroH1) {
        heroH1.style.opacity = '1';
        heroH1.style.visibility = 'visible';
    }

    // ── 9. LAZY IMAGES ──────────────────────────────────────────
    if ('IntersectionObserver' in window) {
        const imgObs = new IntersectionObserver(function (entries, obs) {
            entries.forEach(function (e) {
                if (e.isIntersecting && e.target.dataset.src) {
                    e.target.src = e.target.dataset.src;
                    obs.unobserve(e.target);
                }
            });
        }, { rootMargin: '200px' });
        document.querySelectorAll('img[data-src]').forEach(img => imgObs.observe(img));
    }

    // ── 10. DEFERRED INITS (wait for deferred scripts) ──────────
    window.addEventListener('load', function () {

        // AOS
        if (typeof AOS !== 'undefined') {
            AOS.init({
                duration: 400,
                easing: 'ease-out',
                once: true,
                offset: 60,
                throttleDelay: 150,
            });
        }

        // Swiper — Testimonials
        if (typeof Swiper !== 'undefined' && document.querySelector('.testimonials-swiper')) {
            new Swiper('.testimonials-swiper', {
                slidesPerView: 1,
                spaceBetween: 24,
                loop: true,
                autoplay: { delay: 4000, disableOnInteraction: false },
                pagination: { el: '.swiper-pagination', clickable: true },
                navigation: {
                    nextEl: '.swiper-button-next',
                    prevEl: '.swiper-button-prev',
                },
                breakpoints: {
                    768:  { slidesPerView: 2 },
                    1024: { slidesPerView: 3 },
                },
            });
        }

        // LightGallery — project detail
        if (typeof lightGallery !== 'undefined') {
            document.querySelectorAll('.project-lightgallery').forEach(function (el) {
                lightGallery(el, {
                    selector: '.gallery-item',
                    speed: 350,
                    download: false,
                });
            });
            const gc = document.querySelector('.gallery-container');
            if (gc) lightGallery(gc, { speed: 350, download: false });
        }

        // GSAP — minimal: only service card hover, no ScrollTrigger
        if (typeof gsap !== 'undefined') {
            document.querySelectorAll('.service-card').forEach(function (card) {
                card.addEventListener('mouseenter', () => gsap.to(card, { y: -8, duration: 0.2, ease: 'power2.out' }));
                card.addEventListener('mouseleave', () => gsap.to(card, { y: 0,  duration: 0.2, ease: 'power2.out' }));
            });
        }

    });

    // ── CSRF helper ─────────────────────────────────────────────
    window.getCsrf = function () {
        return (document.cookie.match('(^|;)\\s*csrftoken\\s*=\\s*([^;]+)') || []).pop() || '';
    };

});
