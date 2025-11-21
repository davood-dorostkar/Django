# Custom User Model in Django 

Using a **custom user model** is highly recommended for any non-trivial Django project. It gives you full control over authentication fields, user data, and future extensibility.


## 1. Introduction

Django provides two main abstract base classes for building custom users:

### **AbstractUser**

* Extends Django’s default user model.
* Includes fields like `username`, `first_name`, `last_name`, etc.
* Good when you want to **modify** the default model but keep username.

### **AbstractBaseUser**

* Only provides:

  * `password`
  * `last_login`
  * authentication-related behavior
* Used when you want **full control** over fields (e.g., using email instead of username).

### **PermissionsMixin**

* Adds Django’s permission fields and helpers:

  * `is_superuser`
  * `groups`
  * `user_permissions`


## 2. Project Structure

Minimal structure for a custom user app (e.g., `accounts`):

```
accounts/
    models.py
    managers.py
    admin.py
    forms.py       (optional)
```

Then add the app to `INSTALLED_APPS` and set the user model:

```python
AUTH_USER_MODEL = "accounts.CustomUser"
```

### What does `AUTH_USER_MODEL` mean?

It tells Django to use this model **everywhere** authentication is needed:

* migrations
* user creation
* admin authentication
  This **must be set before your first migration**.


## 3. Defining the Custom User Model

```python
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_verified = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
```

### Explanation

* **`email`** → main login field (unique).
* **`is_staff`** → needed for admin login.
* **`is_active`** → deactivate account without deletion.
* **`is_verified`** → useful for email verification workflows.
* **`is_superuser`** → provided by `PermissionsMixin`.
* **`password` is not declared** because `AbstractBaseUser` already includes it.
* **`USERNAME_FIELD`** tells Django to use email for authentication.
* **`REQUIRED_FIELDS`** is used during createsuperuser; here it’s empty.


## 4. Django Translations 

Using:

```python
from django.utils.translation import gettext_lazy as _
```

allows all text wrapped in `_("")` to be translated automatically depending on the site's language settings. Example:

```python
_("email address")
```


## 5. Creating a Custom User Manager

Django requires a manager implementing `create_user` and `create_superuser`.

```python
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(email, password, **extra_fields)
```

### Explanation

* `normalize_email` ensures standard formatting.
* `set_password` hashes the password.
* `create_superuser` enforces required superuser permissions.
* `BaseUserManager` provides email utilities and infrastructure.

### What is a Manager?

A **manager** controls how objects are created or queried.
For users, it's responsible for:

* standard users
* superusers
* custom login rules

More reading:

* [https://docs.djangoproject.com/en/4.0/topics/auth/customizing/](https://docs.djangoproject.com/en/4.0/topics/auth/customizing/)
* [https://testdriven.io/blog/django-custom-user-model/](https://testdriven.io/blog/django-custom-user-model/)
* [https://learndjango.com/tutorials/django-custom-user-model](https://learndjango.com/tutorials/django-custom-user-model)


## 6. Registering Custom User in Django Admin

```python
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email", "is_staff", "is_active")
    list_filter = ("email", "is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2",
                "is_staff", "is_active", "groups", "user_permissions",
            ),
        }),
    )

    search_fields = ("email",)
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)
```

### Explanation

* **`fieldsets`** → fields shown when editing a user.
* **`add_fieldsets`** → fields shown when creating a user.
* Required fields like `password2` **cannot be removed**, because `UserAdmin` expects them.


## 7. Optional: Custom Forms for Admin

Not required, but you can override them:

```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)
```

And plug them into admin:

```python
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
```

More reading:

* [https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#a-full-example](https://docs.djangoproject.com/en/4.2/topics/auth/customizing/#a-full-example)
* [https://docs.djangoproject.com/en/4.2/ref/contrib/admin/](https://docs.djangoproject.com/en/4.2/ref/contrib/admin/)


## 8. Doing Actions on User Creation (Signals)

Signals allow you to run code automatically when a user is created or updated.
Example uses:

* create a Profile model automatically
* send activation email
* log activity

For more info See the [signals](/tutorial/signal.md) documentation
