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

## Model Relationships

Django supports different relationships between tables:

![](/tutorial/img/db-relation-fields.png)

* **ForeignKey** → Many-to-one relationship
* **ManyToManyField** → Many-to-many relationship
* **OneToOneField** → One-to-one relationship


### 1. ForeignKey (Many-to-One)

Example: A blog post belongs to one author, but one author can have many posts.

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

* `on_delete=models.CASCADE` → If the author is deleted, all related posts are also deleted.


### 2. ManyToManyField (Many-to-Many)

Example: A blog post can have multiple tags, and a tag can belong to multiple posts.

```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
```

* Django automatically creates a **join table** to manage this relationship.


### 3. OneToOneField (One-to-One)

Example: Each user has exactly one profile.

```python
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    avatar = models.ImageField(upload_to="avatars/")
```

* Deleting the user will also delete the profile.


## Read More

* [Foreign Key](https://www.geeksforgeeks.org/python-relational-fields-in-django-models/)
* [Many-to-Many Key](https://www.geeksforgeeks.org/python-relational-fields-in-django-models/)
* [One-to-One Key](https://www.geeksforgeeks.org/python-relational-fields-in-django-models/)
