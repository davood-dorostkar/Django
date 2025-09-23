# Using Model Data

## Displaying Data from the Database

You can fetch data from the database and display it in templates.
**Example:** Show the last 4 published blog posts:

```python
posts = Post.objects.filter(published=True).order_by('-date')[:4]
```

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

