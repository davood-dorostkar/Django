# **Getting the User Model in Django**

When working with relationships (e.g., `ForeignKey`, `ManyToManyField`, etc.), you often need to reference the **User** model.
But **Django allows customizing the User model**, so hardcoding it can break your code later.

Django provides **three ways** to access the User model. Here is what each one does, when to use it, and code examples.


## 🔥 **Method 1: Import the User model directly (NOT recommended)**

```python
from accounts import User   # or from django.contrib.auth.models import User

class ModelName(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

### ✔️ Pros

* Simple and direct.

### ❌ Cons

* **Hardcoded** — breaks if you switch to a custom user model.
* Not recommended in production.

**Use this only in very small projects or for quick testing.**


## 🔥 **Method 2: Use `settings.AUTH_USER_MODEL` (recommended in models)**

```python
from django.conf import settings

class ModelName(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
```

### ✔️ Pros

* The **best way to reference a user model inside models.py**.
* Works even if you change the user model later.
* Django recommends using this inside model definitions.

### ❗ Note

`settings.AUTH_USER_MODEL` returns a **string**, like:

```
"accounts.CustomUser"
```


## 🔥 **Method 3: Use `get_user_model()` (recommended outside models)**

```python
from django.contrib.auth import get_user_model

User = get_user_model()

class ModelName(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

### ✔️ Pros

* Gives you the **actual User class**, not a string.
* Perfect for **views, serializers, forms, admin, and business logic**.
* Works with custom user models.

### ❗ Note

Inside `models.py`, `get_user_model()` technically works, but Django recommends `settings.AUTH_USER_MODEL` because it avoids import timing issues.


# ✅ **Summary Table**

| Method                         | What it returns           | Best used in            | Safe with custom user? | Recommended? |
| ------------------------------ | ------------------------- | ----------------------- | ---------------------- | ------------ |
| **Direct import**              | User class                | Small/simple projects   | ❌ No                   | ❌ No         |
| **`settings.AUTH_USER_MODEL`** | `"app.CustomUser"` string | **Models** (ForeignKey) | ✔️ Yes                 | ✔️ **Yes**   |
| **`get_user_model()`**         | User class                | Views, forms, admin     | ✔️ Yes                 | ✔️ Yes       |


# ⭐ Best Practice (short answer)

* **Inside models:**
  👉 Use `settings.AUTH_USER_MODEL`

* **Everywhere else:**
  👉 Use `get_user_model()`
