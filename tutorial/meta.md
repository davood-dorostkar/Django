# Django Model Meta Class

In Django, you can customize the **behavior of your models** using an inner class called **`Meta`**.

Unlike customizing the **Admin view** (which only affects how models are displayed in the admin panel), the **Meta class** changes how the model itself behaves in the database and in queries.


## 1. Defining a Meta Class

The `Meta` class is defined **inside your model class**:

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        ordering = ["name"]  # Example option
```


## 2. Common Meta Options

Here are some of the most useful options you can set in the `Meta` class:


### **1. `abstract`**

Marks a model as **abstract**, so it won’t create its own table. Instead, other models can inherit its fields.

```python
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Student(BaseModel):
    name = models.CharField(max_length=100)
```

➡️ `BaseModel` won’t have its own table; only `Student` will.


### **2. `verbose_name` & `verbose_name_plural`**

Gives human-readable names for the model (useful in admin and elsewhere).

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Learner"
        verbose_name_plural = "Learners"
```

➡️ In the admin, Django will display **“Learner”** and **“Learners”** instead of “Student” and “Students”.


### **3. `app_label`**

Specifies which app this model belongs to (useful if the model is in a different module).

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        app_label = "school"
```


### **4. `ordering`**

Defines default ordering for query results.

```python
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    class Meta:
        ordering = ["age"]         # Ascending by age
        # ordering = ["-age"]      # Descending by age
```

➡️ Now `Student.objects.all()` will always return results ordered by `age`.


### **5. `proxy`**

Creates a **proxy model** that doesn’t create a new table but changes behavior.

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class StudentProxy(Student):
    class Meta:
        proxy = True
        ordering = ["name"]
```

➡️ `StudentProxy` will use the same table as `Student`, but with a different default ordering.


### **6. `permissions`**

Adds custom permissions for your model.

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        permissions = [
            ("can_view_grades", "Can view student grades"),
        ]
```

➡️ You can now assign **“can\_view\_grades”** permission to specific users or groups.


## 3. Summary

| Option                    | Purpose                                        |
| ------------------------- | ---------------------------------------------- |
| **abstract**              | Makes a base class that doesn’t create a table |
| **verbose\_name**         | Human-readable singular name                   |
| **verbose\_name\_plural** | Human-readable plural name                     |
| **app\_label**            | Assigns model to a specific app                |
| **ordering**              | Default ordering of query results              |
| **proxy**                 | Creates a proxy model without a new table      |
| **permissions**           | Adds custom permissions                        |


## 4. Read More

📖 [Django Model Meta options (official docs)](https://docs.djangoproject.com/en/3.2/ref/models/options/)
