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

⚠️ If you don't define `MEDIA_ROOT`, django will use the base project directory as media path. Effectively the media files will be located besides your apps' folders. For example if you define in the DB (and you didn't define `MEDIA_ROOT`):
```py
class Image(models.Model):
    image = models.ImageField(upload_to="img/")
```

your files will be like:
```
.
├── app
├── db.sqlite3
├── img
├── manage.py
├── project
└── requirements.txt
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

## How Statics are Handled in Production vs Development

### 1. Development mode (with `DEBUG=True`)

* In development, Django uses **`django.contrib.staticfiles`** app.
* That app has a special **static file finder system**:

  * It looks inside each app’s `static/` folder.
  * It also looks inside any directories you’ve added to `STATICFILES_DIRS`.
* During development, the **`runserver`** command serves those files directly — no need to run `collectstatic`.

That’s why your project works fine without `collectstatic` in development.

### 2. Production mode (with `DEBUG=False`)

* Django **does not serve static files** in production (for performance and security reasons).
* You need a web server (e.g., Nginx, Apache, or a CDN) to serve static files.
* But those servers don’t know how to search through all your apps for scattered `static/` directories.

That’s why Django provides **`collectstatic`**:

* It gathers all static files from each app and from `STATICFILES_DIRS`.
* It copies them into a single directory (`STATIC_ROOT`).
* Your web server can then serve everything from that one place.


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

        # Media files location - served directly by Nginx
        location /media/ {
            alias /path/to/myproject/media/;
            expires 1d;
            add_header Cache-Control "public";
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

## Django Template Tags for Static Files

### What are Static Tags?

`{% load static %}` enables you to use `{% static 'path/to/file' %}` inside templates.

Example:

```html
{% load static %}
<link rel="stylesheet" href="{% static 'myapp/css/style.css' %}">
```
