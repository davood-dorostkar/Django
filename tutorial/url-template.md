# Dynamic URL (URL Templates)

Hardcoding links in your HTML (`<a href="/blog/post/1/">`) is fragile — if your URL structure changes, you’d have to update it everywhere.

Instead, Django provides the **`{% url %}` template tag**, which dynamically generates URLs using the **view name** defined in `urls.py`.


## Defining URL Names in `urls.py`

Each `path()` can be given a `name`.
Example: `blog/urls.py`

```python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

Here we defined a named URL:

* `"index"` → `/blog/`


## Using `{% url %}` in Templates

Now, instead of hardcoding paths, use `{% url %}` with the **view name**.

### Example in HTML

```django
<ul>
    <li><a href="{% url 'blog:index' %}">Home</a></li>
</ul>
```

This generates:

```html
<ul>
    <li><a href="/blog/">Home</a></li>
</ul>
```


## URL Namespaces

If multiple apps define views with the same name (e.g., both `blog` and `shop` apps have an `"index"` view), Django uses **namespaces** to distinguish them.

Namespaces are enabled by setting `app_name` inside `urls.py`.

### Example with namespaces

**blog/urls.py**

```python
app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
]
```

**shop/urls.py**

```python
app_name = "shop"

urlpatterns = [
    path("", views.index, name="index"),
]
```

**main urls.py**

```python
from django.urls import path, include

urlpatterns = [
    path("blog/", include("blog.urls")),
    path("shop/", include("shop.urls")),
]
```

**In templates**

```django
<a href="{% url 'blog:index' %}">Go to Blog</a>
<a href="{% url 'shop:index' %}">Go to Shop</a>
```


## Passing Parameters to `{% url %}`

If a view takes parameters (like `post_id`), pass them in the same order (positional) or as keywords.

### Defining Parameters in `urls.py`
```python
from django.urls import path
from . import views

app_name = "blog"  

urlpatterns = [
    path("<int:post_id>/", views.detail, name="detail"),
]
```

### Positional arguments

```django
<a href="{% url 'blog:detail' 42 %}">Read Post 42</a>
```

### Keyword arguments

```django
<a href="{% url 'blog:detail' post_id=42 %}">Read Post 42</a>
```

Both resolve to:

```html
<a href="/blog/post/42/">Read Post 42</a>
```


## Best Practices

✅ Always use `{% url %}` instead of hardcoding links.
✅ Use `app_name` in each app’s `urls.py` to avoid naming conflicts.
✅ Prefer **keyword arguments** for readability.
✅ If you rename or restructure URLs, templates won’t break as long as names remain consistent.


## Quick Example: Full Setup

**blog/urls.py**

```python
app_name = "blog"

urlpatterns = [
    path("", views.index, name="index"),
    path("post/<int:post_id>/", views.detail, name="detail"),
]
```

**blog/views.py**

```python
from django.shortcuts import render

def index(request):
    return render(request, "blog/index.html")

def detail(request, post_id):
    return render(request, "blog/detail.html", {"post_id": post_id})
```

**blog/templates/blog/index.html**

```django
<h1>Blog Home</h1>
<ul>
    <li><a href="{% url 'blog:index' %}">Home</a></li>
    <li><a href="{% url 'blog:detail' post_id=1 %}">First Post</a></li>
</ul>
```


✅ With this setup, Django generates the correct URLs automatically, even if you later change `/blog/` to `/articles/`.
