# 🌐 Using cPanel for Django Deployment

## 📖 Intro to cPanel

cPanel is a popular **web hosting control panel** that simplifies server management through a graphical interface.

* [What is cPanel? (UIllinois)](https://answers.uillinois.edu/illinois/page.php?id=84995)
* [Beginner’s Guide (Hostinger)](https://www.hostinger.com/tutorials/what-is-cpanel)


## 🚀 Deploying Django on cPanel

### 1. Install Python

Enable Python from your hosting provider’s cPanel dashboard.

### 2. Setup Your Project

* Either **create** your Django project in the terminal, or **upload** an existing one.
* Install dependencies:

  ```bash
  pip install -r requirements.txt
  ```

### 3. Configure `passenger.wsgi`

This file tells the server how to run your Django app. Example:

```python
import sys, os
sys.path.append('/home/username/myproject')
os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

### 4. Handle Static & Media Files

cPanel requires serving static/media files from `public_html/`.
Update `settings.py`:

```python
STATIC_ROOT = "/home/username/public_html/static"
MEDIA_ROOT = "/home/username/public_html/media"
```

Then collect static files:

```bash
python manage.py collectstatic
```

🔎 More details: [Static & Media in Production](/tutorial/static-media.md#how-statics-are-handled-in-production-vs-development)


## 📚 Read More

* [A2Hosting Guide](https://www.a2hosting.com/kb/developer-corner/python/installing-and-configuring-django-on-linux-shared-hosting)
* [DotRoll Tutorial](https://dotroll.com/en/knowledge-base/install-and-run-python-django-using-cpanel/)
* [Medium Guide](https://medium.com/@pyzimos/deploying-django-web-application-using-cpanel-6687b8057439)
