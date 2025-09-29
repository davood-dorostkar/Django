# Deploying Django Applications

Django can run in development with its built-in server, but for **production** you need a proper deployment setup with WSGI/ASGI servers and security configurations.

This guide covers:

1. **WSGI Deployment**
2. **ASGI Deployment**
3. **Deployment Checklist**


## 1. WSGI Deployment

WSGI (**Web Server Gateway Interface**) is the traditional way to serve Django applications.

* Works with **synchronous** Django views.
* Common servers: **Gunicorn**, **uWSGI**, **mod_wsgi (Apache)**.

### Example (Gunicorn + Nginx):

```bash
pip install gunicorn
gunicorn myproject.wsgi:application
```

Then configure **Nginx** (or another reverse proxy) to forward requests to Gunicorn.


## 2. ASGI Deployment

ASGI (**Asynchronous Server Gateway Interface**) is the modern standard.

* Supports **both sync and async** views (WebSockets, long-lived connections, background tasks).
* Common servers: **Daphne**, **Uvicorn**, **Hypercorn**.

### Example (Uvicorn):

```bash
pip install uvicorn
uvicorn myproject.asgi:application --host 0.0.0.0 --port 8000
```

You can also run it behind **Nginx** for load balancing and static file handling.


## 3. Deployment Checklist

Before deploying, run:

```bash
python manage.py check --deploy
```

This command checks for common production misconfigurations.

### Key items to review:

* **DEBUG** must be `False`.
* **ALLOWED_HOSTS** must be set (e.g. your domain, server IP).
* **SECRET_KEY** must be kept secret and not hardcoded.
* Use **secure cookies** (`CSRF_COOKIE_SECURE`, `SESSION_COOKIE_SECURE`).
* Use **HTTPS** (with SSL/TLS).
* Proper **logging** and **error monitoring**.
* Serve **static files** and **media files** via web server or CDN.


## Additional Resources

* [Django Deployment Docs](https://docs.djangoproject.com/en/5.2/howto/deployment/)
* [Django Deployment Checklist](https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/)
* [MDN: Django Deployment](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment)
* [Simple is Better than Complex: Production Setup](https://simpleisbetterthancomplex.com/tutorial/2021/06/27/how-to-start-a-production-ready-django-project.html)
* [Thinkster: Configuring Django Settings for Production](https://thinkster.io/tutorials/configuring-django-settings-for-production)


✅ With this, you know how to deploy Django via **WSGI or ASGI**, and how to **harden your project for production**.
