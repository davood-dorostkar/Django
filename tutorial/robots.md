# 🤖 Robots.txt in Django

## 1. What is `robots.txt`?

* `robots.txt` is a special file that tells **search engine crawlers** (Googlebot, Bingbot, etc.) how they should interact with your website.
* It controls which parts of your site should be **indexed or ignored**, helping manage SEO and reduce unnecessary crawling.

Example:

```
User-agent: *
Disallow: /admin/
Allow: /blog/
Sitemap: https://example.com/sitemap.xml
```


## 2. Django Robots Package

Django does not generate `robots.txt` by default. For dynamic and admin-managed rules, you can use the **django-robots** package.

### Installation & Setup

1. Install the package:

   ```bash
   pip install django-robots
   ```

2. Add to `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       ...
       "django.contrib.sites",
       "robots",
   ]
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

4. Add to your `urls.py`:

   ```python
   from django.urls import path, include

   urlpatterns = [
       ...
       path("robots.txt", include("robots.urls")),
   ]
   ```

👉 At this point, `robots.txt` will be **generated automatically** based on the rules you define in the Django admin.


## 3. How It Works

* Depends on the **Sites Framework** (each site can have its own `robots.txt` rules).
* Once added and migrated, it creates **database tables** to store robot rules.
* You can manage rules via the Django **Admin interface** without editing files.


## 4. Robots File Sections

A `robots.txt` file usually contains these sections:

* **User-agent** → Defines which crawlers the rule applies to (`*` = all crawlers).
* **Host** → The preferred domain for indexing.
* **Allow** → Paths that crawlers are permitted to access.
* **Disallow** → Paths that crawlers must not index.
* **Sitemap** → URL of your sitemap (`sitemap.xml`).


## 5. Django Robots Settings

You can configure some global defaults in `settings.py`:

* `ROBOTS_USE_SITEMAP = True` → automatically add sitemap location if available.
* `ROBOTS_USE_HOST = True` → include host definition.
* `ROBOTS_CACHE_TIMEOUT = 60*60*24` → cache robots.txt for better performance.

👉 Fine-grained rules are usually defined via **Admin > Robots > Rules**.


## 6. Example

In Django Admin, you might define:

* **User-agent**: `*`
* **Disallow**: `/admin/`
* **Allow**: `/blog/`
* **Sitemap**: `https://example.com/sitemap.xml`

This will generate:

```
User-agent: *
Disallow: /admin/
Allow: /blog/
Sitemap: https://example.com/sitemap.xml
```


## 7. Read More

* [Django Robots Docs](https://django-robots.readthedocs.io/en/latest)
* [PyPI – django-robots](https://pypi.org/project/django-robots)
