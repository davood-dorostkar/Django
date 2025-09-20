# Model Relationships

Django supports different relationships between tables:

![](/tutorial/img/db-relation-fields.png)

* **ForeignKey** → Many-to-one relationship
* **ManyToManyField** → Many-to-many relationship
* **OneToOneField** → One-to-one relationship

## 1. ForeignKey (Many-to-One)

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
* `on_delete=models.SET_NULL` → If the author is deleted, all related posts' authors will be set to null.

## 2. ManyToManyField (Many-to-Many)

Example: A blog post can have multiple tags, and a tag can belong to multiple posts.

```python
class Tag(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag)
```

* Django automatically creates a **join table** to manage this relationship.

## 3. OneToOneField (One-to-One)

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
