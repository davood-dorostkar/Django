# 🏷️ Django Taggit Module

## 1. What is Taggit?

[`django-taggit`](https://django-taggit.readthedocs.io/en/latest/getting_started.html) is a **third-party Django app** that makes it easy to add **tags** to your models.

* Tags let you categorize and organize content (e.g., blog posts, products).
* Provides a simple and flexible **many-to-many relationship** between your objects and tags.


## 2. Installation & Setup

1. Install the package:

   ```bash
   pip install django-taggit
   ```

2. Add to your `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       ...
       "taggit",
   ]
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```


## 3. Usage in Models

To enable tagging on a model:

```python
from django.db import models
from taggit.managers import TaggableManager

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = TaggableManager()  # ✅ Enables tagging
```

* A **`tags` field** will now be available.
* Each `BlogPost` can have multiple tags.


## 4. Adding & Accessing Tags

```python
post = BlogPost.objects.create(title="Django Tips", content="...")
post.tags.add("django", "tutorial", "webdev")   # add multiple tags
post.tags.all()                                 # get all tags
post.tags.remove("tutorial")                    # remove a tag
```

* Under the hood, Taggit creates **extra tables** for storing tags and relationships.


## 5. Filtering by Tags

You can query objects by tags:

```python
# all posts tagged with "django"
posts = BlogPost.objects.filter(tags__name__in=["django"])
```


## 6. Example View & Template

### View:

```python
from django.shortcuts import render
from .models import BlogPost

def posts_by_tag(request, tag_name):
    posts = BlogPost.objects.filter(tags__name__in=[tag_name])
    return render(request, "blog/posts_by_tag.html", {"posts": posts, "tag": tag_name})
```

### Template:

```django
<h2>Posts tagged with "{{ tag }}"</h2>
<ul>
  {% for post in posts %}
    <li>{{ post.title }}</li>
  {% empty %}
    <li>No posts found for this tag.</li>
  {% endfor %}
</ul>
```


## 7. Advanced Features

* **Tag suggestions**: Get frequently used tags.
* **Slug support**: Use tag slugs in URLs (`/tags/django/`).
* **Custom tag models**: Extend `TagBase` for advanced use cases.


## 8. Read More

* [Django Taggit Docs](https://django-taggit.readthedocs.io/en/latest/getting_started.html)
* [GitHub Repo](https://github.com/jazzband/django-taggit)
