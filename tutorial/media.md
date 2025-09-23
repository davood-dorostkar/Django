# 📁 Handling Media Files in Django

Django allows you to serve two types of extra files alongside your HTML templates:

1. **Static files** – Files that rarely change, like CSS, JS, or global images.
2. **Media files** – Files uploaded by users, which can be dynamic (e.g., profile pictures, post images).

This tutorial focuses on **media files**, specifically **image handling**, but also touches on related static file handling.


## 1. Configuring Media in Django

In `settings.py`, define:

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Media files (user-uploaded content)
MEDIA_URL = '/media/'           # URL to access media
MEDIA_ROOT = BASE_DIR / 'media' # Directory where uploaded files are stored
```

Then in `urls.py`, make sure Django can serve media files during development:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # ... other urls ...
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

> ⚠️ In production, a web server (e.g., Nginx) should serve media files directly for better performance.


## 2. Installing Pillow

Django uses the **Pillow** library to work with image files. Install it with:

```bash
pip install pillow
```


## 3. Using `ImageField` in Models

You can add images to your models using `ImageField`:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', default='default.jpg')
```

### Key Points:

* The **image is stored on disk** (inside `MEDIA_ROOT`)
* The **database only stores the file path**
* If the same filename exists, Django automatically renames it to avoid conflicts


### `upload_to` Option

* Default behavior: saves images in `MEDIA_ROOT`
* Custom folder: relative path inside `MEDIA_ROOT`

```python
image = models.ImageField(upload_to='posts/')
```

* Organize uploads by date:

```python
image = models.ImageField(upload_to='posts/%Y/%m/%d/')
```

This creates directories like `posts/2025/09/23/`.


### `default` Option

Specify a default image if no file is provided:

```python
image = models.ImageField(upload_to='posts/', default='default.jpg')
```


### Accessing Images in Templates

```html
{% load static %}
<img src="{{ post.image.url }}" alt="{{ post.title }}">
```

> Always use `{% load static %}` at the top of templates that display media or static files.


## 4. Deleting and Updating Images

* Deleting a model instance **does not delete the file from disk**. You must handle file deletion manually if needed.
* Updating an image: Django updates the database path, but old files remain unless deleted explicitly.


## 5. Example: Organizing Uploads

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', default='avatars/default.jpg')
```

This keeps media organized by **year/month/day**.


## 6. Handling Dynamic Media in Views

You can use a **single view for multiple URLs** and handle optional parameters:

```python
# urls.py
path('blog/', views.blog_view, name='blog'),
path('blog/category/<str:category>/', views.blog_view, name='blog-category'),

# views.py
def blog_view(request, category=None):
    posts = Post.objects.all()
    if category:
        posts = posts.filter(category__name=category)
    return render(request, 'blog.html', {'posts': posts})
```

* `category=None` makes the parameter optional
* Dynamic filtering uses **Django ORM queries**


## 7. Filtering, Searching, and Displaying Images

### Filter by attribute

```python
posts = Post.objects.filter(published=True)
```

### Search by term using `__contains`:

```python
query = request.GET.get('q')
if query:
    posts = Post.objects.filter(title__contains=query)
```


## 8. Best Practices

* Always include `{% load static %}` in templates that use static or media URLs
* Organize media folders logically (by model or date)
* Handle file deletions carefully to avoid orphaned files
* Use dynamic views for filtering and search, not hardcoded URLs


## 9. Read More

* [Django: Working with Files](https://docs.djangoproject.com/en/3.2/topics/files/)
* [Django: Static Files](https://docs.djangoproject.com/en/3.2/howto/static-files/)
* [Uploading Images with Django](https://djangocentral.com/uploading-images-with-django/)
* [GeeksforGeeks: ImageField in Django](https://www.geeksforgeeks.org/imagefield-django-models/)

