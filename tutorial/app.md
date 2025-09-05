# Django Apps

In Django, **apps** are modular components that represent a specific piece of functionality in your project. Each app is a self-contained subproject that organizes models, views, templates, static files, and more.

👉 A Django **project** is the overall container (configuration + settings), and it can include **multiple apps**.

For example:

* A `blog` app for managing blog posts.
* A `shop` app for e-commerce.
* A `users` app for authentication.


## Creating an App

To create a new app, use:

```sh
python manage.py startapp app_name
```

This will generate the following structure:

```
app_name/
    admin.py        # Register models for Django admin
    apps.py         # Configuration for the app
    models.py       # Database models
    tests.py        # Tests for this app
    views.py        # Business logic (controllers)
    __init__.py     # Marks directory as a Python package
    migrations/     # Database migration files
```


## Adding the App to the Project

After creating the app, you need to **register it** in your project’s `settings.py`:

```python
INSTALLED_APPS = [
    # default Django apps...
    'app_name',   # add your app here
]
```

If you created the project correctly, your directory tree might look like this:

```
.
├── project/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── app_name/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
```


## App URLs

Each app can have its own **`urls.py`** file to organize routes.

For example, inside your app (`blog/urls.py`):

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="blog_index"),
    path('post/<int:id>/', views.post_detail, name="post_detail"),
]
```

Then include this in the **main `urls.py`**:

```python
from django.urls import path, include

urlpatterns = [
    path('blog/', include('blog.urls')),  # include app urls
]
```

✅ Now:

* `http://HOSTNAME/blog/` → `views.index`
* `http://HOSTNAME/blog/post/3/` → `views.post_detail`


### Important Note About Slashes

Django combines paths exactly as written. Pay close attention to trailing slashes (`/`).

Example 1 (missing slash in main URL):

```python
# project urls.py
urlpatterns = [
    path('app', include('app.urls'))  # ⚠ no trailing slash
]

# app urls.py
urlpatterns = [
    path('blog', views.main_view),
]
```

Result: The final URL is `HOSTNAME/appblog` (no slash between them).

Example 2 (correct way with slash):

```python
# project urls.py
urlpatterns = [
    path('app/', include('app.urls'))  # ✅ with trailing slash
]

# app urls.py
urlpatterns = [
    path('blog', views.main_view),
]
```

Result: Final URL is `HOSTNAME/app/blog`


## `APPEND_SLASH` Setting

Django has a setting called `APPEND_SLASH` (default: `True`).
It is handled by **CommonMiddleware**, and it automatically redirects to a slashed version of the URL if needed.

Example:

```python
urlpatterns = [
    path('blog/', views.main_view),
]
```

### Case 1: `HOSTNAME/blog` (without slash)

* Django sees no match for `blog`
* But `blog/` exists
* Since `APPEND_SLASH = True`, Django redirects to `HOSTNAME/blog/`

![](/tutorial/img/slash-redirect.png)

### Case 2: `HOSTNAME/blog/` (with slash)

* Matches directly, no redirect.

### Case 3: `APPEND_SLASH = False`

* Visiting `HOSTNAME/blog` → **404 error** (no redirect).


### Default Value and Location

Default (in Django’s global settings):

```python
APPEND_SLASH = True
```

You can override it in `settings.py`:

```python
APPEND_SLASH = False  # disables auto-redirect
```


## Summary

* **Apps** are modular pieces of a Django project.
* Create with `python manage.py startapp app_name`.
* Register the app in `INSTALLED_APPS`.
* Use `urls.py` in each app and include it in the project.
* Be careful with trailing slashes in paths.
* `APPEND_SLASH` helps avoid 404s by redirecting missing-slash URLs.
