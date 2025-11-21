# Django Signals

Django **signals** provide a way for decoupled applications to get notified when certain actions occur elsewhere in the framework. A signal sends out a notification (“signal event”), and any connected **receivers** can perform actions in response.

This allows you to keep logic separated while still reacting to events such as model creation, user login, changes in data, and more.


## Common Use Cases for Signals

Signals are useful when you want an action to run automatically after a specific event without modifying the original code directly.

Typical use cases include:

* Automatically creating related objects (e.g., `Profile` after `User` creation)
* Logging or auditing changes
* Sending emails or notifications
* Clearing caches after updates
* Performing cleanup when an object is deleted
* Updating counters or denormalized fields


## Most Common Django Signals

Django provides several built-in signals. The most commonly used include:

### **Model Signals**

* `pre_save` – fired before a model instance is saved
* `post_save` – fired after a model instance is saved
* `pre_delete` – fired before a model is deleted
* `post_delete` – fired after a model is deleted
* `m2m_changed` – fired when a many-to-many relationship changes

### **Authentication Signals**

* `user_logged_in`
* `user_logged_out`
* `user_login_failed`

### **Request/Response Signals**

* `request_started`
* `request_finished`

### **Database Signals**

* `pre_migrate`, `post_migrate`


## Example: Automatically Creating a Profile When a User Is Created

A very common example is creating a `Profile` model linked to Django’s `User` model. When a new user is created, a corresponding profile should be automatically generated.

### 1. Create the `Profile` Model

```python
# accounts/models.py
from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
```

### Register in Admin

```python
# accounts/admin.py
from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
```


## 2. Creating the Profile Using `post_save`

```python
# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    # IMPORTANT: Check if it’s created, otherwise it will run on every save
    if created:
        Profile.objects.create(user=instance)
```


## 3. Connecting the Signal

To ensure Django loads your signals, import them inside your app's `ready()` method.

```python
# accounts/apps.py
from django.apps import AppConfig

class AccountsConfig(AppConfig):
    name = 'accounts'

    def ready(self):
        import accounts.signals
```

And update your **settings**:

```python
INSTALLED_APPS = [
    ...
    'accounts.apps.AccountsConfig',
]
```


## `connect()` vs `@receiver`

Django provides two ways to attach signals.

### Using `connect()` Manually

```python
post_save.connect(create_profile, sender=User)
```

This must be executed at import time, usually in `signals.py`.

### Using the `@receiver` Decorator (Recommended)

```python
@receiver(post_save, sender=User)
def create_profile(...):
    ...
```

The decorator is cleaner, avoids mistakes, and works well with `apps.py` auto-loading.


## Important Note

> Always check whether the instance was **created** when using `post_save`.
> Otherwise, a new Profile would be created on *every* update to the User model.

Correct:

```python
if created:
    Profile.objects.create(user=instance)
```


## Read More

* [simpleisbetterthancomplex – Django Signals](https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html)
* [Django Official Docs – Signals](https://docs.djangoproject.com/en/3.2/topics/signals/)
* [GeeksforGeeks – Django Signals](https://www.geeksforgeeks.org/python/how-to-create-and-use-signals-in-django/)
* [I Love Django – Signals](https://ilovedjango.com/django/models-and-databases/django-signals/)
* [Studygyaan – Create & Use Signals](https://studygyaan.com/django/how-to-use-and-create-django-signals)
