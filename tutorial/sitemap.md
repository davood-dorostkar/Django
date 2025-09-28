# 🗺️ Django Sitemap Framework

The **Sitemap Framework** is a built-in Django app that helps you generate **XML sitemaps** automatically.

* Search engines (Google, Bing, etc.) use sitemaps to **discover and index** your site’s pages more effectively.
* It works by describing the structure of your site and giving hints like how often pages change and when they were last updated.


## 1. Setup

1. Add to **`INSTALLED_APPS`** in `settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       "django.contrib.sites",
       "django.contrib.sitemaps",
   ]
   ```

2. Ensure the **Sites Framework** is already configured (`SITE_ID`, domain in admin).


## 2. What is `reverse`?

* Django’s `reverse()` is used to **dynamically build URLs** from named URL patterns.
* Example:

  ```python
  from django.urls import reverse

  reverse("home")  # returns "/"
  reverse("blog_detail", kwargs={"id": 5})  # returns "/blog/5/"
  ```


## 3. Creating Sitemaps

### A. Static Pages

For pages like "home", "about", "contact":

#### `sitemaps.py`

```python
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"   # how often the page changes
    priority = 0.8           # importance (0.0–1.0)

    def items(self):
        return ["home", "about", "contact"]

    def location(self, item):
        return reverse(item)
```

#### `urls.py`

```python
from django.contrib import sitemaps
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    ...
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"),
]
```


### B. Dynamic Pages

For models like `BlogPost`, where URLs depend on DB entries:

#### `models.py`

```python
from django.db import models
from django.urls import reverse

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={"id": self.id})
```

#### `sitemaps.py`

```python
from django.contrib.sitemaps import Sitemap
from .models import BlogPost

class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.all()

    def location(self, obj):
        return obj.get_absolute_url()

    def lastmod(self, obj):
        return obj.updated
```

#### `urls.py`

```python
from .sitemaps import StaticViewSitemap, BlogPostSitemap

sitemaps = {
    "static": StaticViewSitemap,
    "blog": BlogPostSitemap,
}
```


## 4. Sitemap Attributes

* **`changefreq`** → `always`, `hourly`, `daily`, `weekly`, `monthly`, `yearly`, `never`
* **`priority`** → importance (`0.0` – `1.0`)
* **`items()`** → returns list/queryset of objects or page names
* **`location()`** → URL of each item (can use `reverse` or `get_absolute_url`)
* **`lastmod()`** → returns datetime for last modified pages


## 5. Read More

* [Official Docs – Django Sitemaps](https://docs.djangoproject.com/en/3.2/ref/contrib/sitemaps)
