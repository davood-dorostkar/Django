# Using Database Data, URLs, and Querying in Django

## Displaying Data from the Database

You can fetch data from the database and display it in templates.
**Example:** Show the last 4 published blog posts:

```python
posts = Post.objects.filter(published=True).order_by('-date')[:4]
```


## Dynamic URLs with Parameters

You can pass parameters to views using the URL pattern.

**Example (single parameter):**

```python
# urls.py
path('posts/<int:id>/', views.post_detail, name='post_detail')

# views.py
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post_detail.html", {"post": post})
```

**Example (multiple parameters with static text):**

```python
path('blog/<int:year>/<slug:slug>/', views.post_archive, name='post_archive')
```

📖 [Read more](https://docs.djangoproject.com/en/3.2/topics/http/urls/)


## Getting Objects Safely

Use `get_object_or_404` to fetch objects and return a 404 if not found.

**Example:**

```python
from django.shortcuts import get_object_or_404

post = get_object_or_404(Post, id=uid, published=True)
```

Other similar helpers:

* `get_list_or_404()`


## Filtering Objects

You can filter objects by attributes before querying.

**Example:**

```python
posts = Post.objects.filter(published=True)
```


## Referencing the User Model

Always reference the user model dynamically instead of importing `User` directly.

**Example:**

```python
from django.contrib.auth import get_user_model
User = get_user_model()
```

📖 [Read more](https://learndjango.com/tutorials/django-best-practices-referencing-user-model)

