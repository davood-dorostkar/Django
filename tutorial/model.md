# Django Models

In every Django app, there is a file called **`models.py`**.

Inside this file, you can define **classes** that inherit from the base class `models.Model`.

* The **class name** becomes the **table name** in the database.
* The actual table name will be:

  ```
  appname_classname   (all in lowercase)
  ```
* Each **class member (field)** becomes a **column** in that table.


## Example

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```

This will create a table named **`appname_student`** with columns: `id`, `name`, `age`, `email`.


## Database Visualization

* You can design your database before coding using tools like **[DrawSQL](https://drawsql.app/)**.
* Django also has extensions that can generate a **graphical view of your models** automatically.


## Common Model Fields

![](/tutorial/img/db-field-names.png)

>By default, the `id` field is generated automatically from 1 and increasing. When you delete an object, django knows that that id is deleted and must not be used again.

## Model Options

![](/tutorial/img/db-field-options.png)

* Some fields have **mandatory options**, like `max_length` for `CharField`.
* Useful options:

  * `auto_now_add=True` → Sets the timestamp when the record is **created**.
  * `auto_now=True` → Updates the timestamp every time the record is **updated**.

⚠️ If a field requires a default and you don’t provide one, Django will ask you to:

* Either set a **permanent default value**, or
* Enter a **temporary default** for migrations.

🔑 **`blank=True` vs `null=True`**

* `blank=True` → Field can be empty in **forms**.
* `null=True` → Field can store **NULL values** in the database.

### Example
```py
class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
```

## Model Methods
We can also define methods in a model or override existing ones (like `__str__`).

```py
class Post(models.Model):
  …
  def __str__(self):
        return self.title
```
