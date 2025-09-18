# Django Admin

The **Django Admin** is a built-in interface that allows you to manage your database models using a friendly web interface.

By default, you can access it at:

```
http://localhost:8000/admin
```


## 1. Registering Models

To make a model visible in the admin interface, register it in the **`admin.py`** file of the app:

### Example (basic registration)

```python
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

### Example (using a decorator with customization)

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    ...
```


## 2. Improving Display with `__str__`

By default, Django shows entries using their **ID**, which is not very readable:

![](/tutorial/img/admin-before.png)

You can change this by overriding the **`__str__`** method in your model:

```python
class Post(models.Model):
    title = models.CharField(max_length=255)
    ...

    def __str__(self):
        return self.title
```

Now the objects will display with their **title** instead:

![](/tutorial/img/admin-after.png)


## 3. Customizing the Admin Interface

Django allows many ways to customize how your models appear in the admin.

### Show fields in the list view

```python
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "counted_views", "status", "published_date", "created_date")
```

![](/tutorial/img/admin-list-display.png)


### Add filters in the sidebar

```python
list_filter = ("status",)
```

![](/tutorial/img/admin-list-filter.png)


### Add search functionality

```python
search_fields = ["title", "content"]
```

![](/tutorial/img/admin-search.png)


### Date hierarchy navigation

```python
date_hierarchy = "published_date"
```

![](/tutorial/img/admin-date-hierarchy.png)


### Handle empty values

```python
empty_value_display = "-empty-"
```

![](/tutorial/img/admin-empty-value.png)


### Control which fields appear

* **fields** → specify which fields to show.
* **exclude** → hide specific fields.

```python
fields = ("title", "content", "status")
exclude = ("counted_views",)
```


### Ordering entries

```python
ordering = ("-created_date",)
```


## 4. Summary of Useful Options

Inside `PostAdmin` (or any ModelAdmin class), you can use:

* `list_display` → show specific fields in list view.
* `list_filter` → add sidebar filters.
* `search_fields` → search by fields.
* `date_hierarchy` → add date navigation.
* `ordering` → set default ordering.
* `fields` / `exclude` → control form fields.
* `empty_value_display` → handle empty values.


## Read More

📖 [Django Admin official documentation](https://docs.djangoproject.com/en/3.2/ref/contrib/admin/)
