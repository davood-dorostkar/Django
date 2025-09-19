# Interacting with Models

Let’s consider this model:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
```

Django ORM allows us to **Create, Retrieve, Update, and Delete (CRUD)** records using Python objects instead of raw SQL queries.


## 1. Create

To create a new row in the database, first create an instance of the model:

```python
from blog.models import Post

p = Post()
p.title = "Django"
p.content = "Text of the post"
```

Save it to the database:

```python
p.save()
```

✅ A new row is now created in the **`post`** table.


## 2. Retrieve

Get **all objects**:

```python
posts = Post.objects.all()
```

* Returns a **QuerySet** (similar to a list).

Filter objects:

```python
published = Post.objects.filter(status=True)
```

Get a single object:

```python
post = Post.objects.get(id=1)
```

⚠️ `.get()` will throw an **error** if no object is found (or if more than one matches).


## 3. Update

Fetch the object, modify its fields, and save:

```python
p = Post.objects.get(id=1)
p.title = "Updated title"
p.save()
```

✅ The row in the database is updated.


## 4. Delete

Delete an object:

```python
p = Post.objects.get(id=1)
p.delete()
```

⚠️ The object is **removed from the database** but still exists in the program memory until the shell is killed:

```python
p.title = "Python"
# This won’t be in the DB anymore, only in memory.
```


## 5. Other Useful ORM Methods

* **Ordering results**

```python
Post.objects.order_by("created_date")      # ascending
Post.objects.order_by("-created_date")     # descending
```

* **Counting results**

```python
Post.objects.count()
```

* **Limiting results**

```python
Post.objects.all()[:5]   # first 5 posts
```

* **Exclude results**

```python
Post.objects.exclude(status=True)   # all drafts
```

* **Exists check**

```python
Post.objects.filter(title="Django").exists()
```

## Summary

* `save()` → Insert or update record.
* `delete()` → Remove record from database.
* `.all()`, `.filter()`, `.get()` → Retrieve records.
* QuerySets behave like **lists**, but are powerful database queries under the hood.

✅ With Django ORM, you can manage your database using **Python objects** instead of writing raw SQL.

## Read More
A good reference of django model queries:

[link](https://docs.djangoproject.com/en/3.2/ref/models/querysets/)
