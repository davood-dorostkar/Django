# Static and Media Files in Django

## Intro
Django projects often require **extra files** beyond templates:

* **Static files**: CSS, JavaScript, images, icons, etc. (don’t change per user)
* **Media files**: User-uploaded files such as profile pictures, documents, or videos

## Static Files: Two Approaches

1. **Internal (self-hosted)** – Static files are stored in your project and served by your server (during development) or a web server like **Nginx**/**Apache** in production.
2. **External (via CDN)** – Use a Content Delivery Network (CDN) like Bootstrap’s hosted CSS/JS for better performance.

### Example: Bootstrap via CDN
```html
<head>
   <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">

</head>
<body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
</body>
```

## Static File Settings

### 1. `STATIC_URL`

Defines the base URL for serving static files in development and production. It defines the **app-specific** path for static files, which means that the final rendered path will be relative to the app folder.


**Example**:
```python
STATIC_URL = '/static/'  # Local 
# or
STATIC_URL = 'https://cdn.example.com/static/'  # with CDN
```

**In templates**:
```html
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
<!-- Renders to: /static/images/logo.png -->
```

### 2. `STATICFILES_DIRS`

Additional locations Django should look for static files **besides app-level static folders**.

```python
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Project-level static folder
]
```

Django looks for requested files in:

1. Each app’s `static/` folder
2. Any directories listed in `STATICFILES_DIRS`

>when we define `STATIC_URL`, it automatically appends this variable to all apps paths. then the variable `static` (loaded in htmls) will contain a list of all those paths (in addition to `STATICFILES_DIRS`). so practically the path `{% static 'images/logo.png' %}` looks inside static paths and tries fetch the path `'images/logo.png'` relative to them.

### 3. `STATIC_ROOT`

Defines the destination where Django **collects all static files** for production when you run:

```bash
python manage.py collectstatic
```

**Example**:
```python
STATIC_ROOT = '/var/www/example.com/static/'
# or
STATIC_ROOT = BASE_DIR / 'staticfiles' 
```

Then a web server (e.g., Nginx) serves files directly from this folder.

## Media Files Settings

Media files are **uploaded by users**, so they need separate handling. 

```py
MEDIA_URL = '/media/'   # URL prefix
MEDIA_ROOT = BASE_DIR / 'media'  # Folder to store uploaded 
```

**Example usage in a template**:

```html
<img src="{{ user.profile.image.url }}" alt="Profile picture">
```

## Adding Static and Media to URLs

In `urls.py`, during **development**, serve static & media files like this:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

⚠️ In **production**, let your web server (Nginx/Apache) serve these files instead.

## Django Static Files Workflow Example

### Project Structure

```
myproject/
├── myapp/
│   ├── static/myapp/css/style.css
│   ├── static/myapp/js/script.js
│   └── static/myapp/images/logo.png
├── static/global.css
└── staticfiles/   # created by collectstatic in production
```

### Configuration (settings.py)

```python
# Development settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Project-level static files
]

if DEBUG == False:
    # Production settings 
    STATIC_ROOT = BASE_DIR / 'staticfiles'
```

### Template File (index.html)

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
    <link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
    <link rel="stylesheet" href="{% static 'global.css' %}">
</head>
<body>
    <h1>Welcome to My App</h1>
</body>
</html>
```

### Complete Workflow with Browser

#### 1. In Development (runserver)

* User visits `http://localhost:8000/`
* Django looks inside `myapp/static/` and `STATICFILES_DIRS` (`/static/`)
* Serves files directly via `runserver`
```
Browser Request: GET http://localhost:8000/
↓
Django serves template: index.html
↓
Browser parses HTML and finds:
- {% static 'myapp/css/style.css' %} → /static/myapp/css/style.css
- {% static 'global.css' %} → /static/global.css
↓
Browser makes additional requests:
GET http://localhost:8000/static/myapp/css/style.css
GET http://localhost:8000/static/global.css
↓
Django development server finds and serves these files from:
- /myapp/static/myapp/css/style.css (app-specific)
- /static/global.css (project-level)
```

#### 2. In Production  

- Run `collectstatic` → all static files copied into `STATIC_ROOT` (`/staticfiles/`)
- Creates this structure:
  ```
  staticfiles/
  ├── myapp/
  │   ├── css/
  │   │   └── style.css
  │   ├── js/
  │   │   └── script.js
  │   └── images/
  │       └── logo.png
  └── global.css
  ```
- Configure Nginx to serve `/static/` and `/media/` from these directories
    ```nginx
    server {
        listen 80;
        server_name example.com;
        
        # Serve static files directly
        location /static/ {
            alias /path/to/myproject/staticfiles/;
            expires 30d;
        }
        
        # Pass dynamic requests to Django
        location / {
            proxy_pass http://localhost:8000;
            proxy_set_header Host $host;
        }
    }
    ```


```
Browser Request: GET https://example.com/
↓
Nginx receives request → passes to Django (Gunicorn)
↓
Django serves template: index.html
↓
Browser parses HTML and finds static URLs:
- /static/myapp/css/style.css
- /static/global.css
↓
Browser makes requests to Nginx:
GET https://example.com/static/myapp/css/style.css
GET https://example.com/static/global.css
↓
Nginx serves these files directly from:
- /path/to/myproject/staticfiles/myapp/css/style.css
- /path/to/myproject/staticfiles/global.css
↓
Browser receives static files quickly (no Django processing)
```

## Key Benefits

1. **Performance**: Web server serves static files directly (fast)
2. **Caching**: Static files can be heavily cached
3. **CDN Ready**: Easy to change `STATIC_URL` to CDN URL
4. **Organization**: All static files in one place for deployment

## Jinja & Django Template Language for Static Files

### What are Static Tags?

`{% load static %}` enables you to use `{% static 'path/to/file' %}` inside templates.

Example:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
```


## Jinja vs Django Template Language

Django’s default template engine is **Django Template Language (DTL)**.
It’s **inspired by Jinja2**, but slightly different.

* **Jinja2** is a separate template engine (popular in Flask, can be used in Django).
* **Django Templates** include tags, filters, variables — similar syntax.


### Django Template Syntax Quick Reference

#### Functions (Tags)

```django
{% if user.is_authenticated %}Hello, {{ user.username }}{% endif %}
{% for post in posts %}<p>{{ post.title }}</p>{% endfor %}
{% block content %}{% endblock %}
{% include "header.html" %}
{% extends "base.html" %}
```

#### Data Structures

```django
{{ title }}                <!-- simple variable -->
{{ page.title }}           <!-- object attribute -->
{{ dict.key }}             <!-- dictionary lookup -->
{{ list_items.0 }}         <!-- list index -->
{{ var.upper }}            <!-- method call -->
```

#### Filters

```django
{{ name|title }}                  <!-- capitalize words -->
{{ units|lower }}                 <!-- lowercase -->
{{ post_content|truncatewords:50 }} <!-- shorten text -->
{{ order_date|date:"D M Y" }}     <!-- format date -->
{{ list_items|slice:":3" }}       <!-- slicing -->
{{ item_total|default:"nil" }}    <!-- default value -->
```