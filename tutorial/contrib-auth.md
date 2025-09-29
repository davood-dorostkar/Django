# 🔐 Django Built-in Authentication System

Django provides a **ready-to-use authentication system** that handles login, logout, password reset, and user management. You can extend it with your own templates, views, and forms.


## 1. Setup

### urls.py

Add Django's auth URLs:

```python
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),  # login, logout, password management
]
```

Django provides the following default URLs:

| URL Name                  | Purpose                       |
| ------------------------- | ----------------------------- |
| `login`                   | Login page                    |
| `logout`                  | Logout page                   |
| `password_change`         | Change password page          |
| `password_change_done`    | Password changed confirmation |
| `password_reset`          | Reset password page           |
| `password_reset_done`     | Reset email sent confirmation |
| `password_reset_confirm`  | Password reset confirm page   |
| `password_reset_complete` | Password reset completed page |


## 2. List of Existing URLs

The following URLs are automatically available:

* `accounts/login/` → login
* `accounts/logout/` → logout
* `accounts/password_change/` → change password
* `accounts/password_change/done/` → password change done
* `accounts/password_reset/` → reset password request
* `accounts/password_reset/done/` → reset email sent
* `accounts/reset/<uidb64>/<token>/` → reset password confirm
* `accounts/reset/done/` → password reset done


## 3. Templates Folder

Create a `registration` folder inside your templates directory:

```
templates/
└── registration/
    ├── login.html
    ├── logged_out.html
    ├── password_reset_form.html
    ├── password_reset_done.html
    ├── password_reset_confirm.html
    ├── password_reset_complete.html
```

These templates override Django’s defaults.

### Example `login.html`

```django
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
```

### Example `logout.html`

```django
<h2>Logged out</h2>
<p>You have been logged out successfully.</p>
<a href="{% url 'login' %}">Login again</a>
```


## 4. Use Its Functions and Views

Import from Django’s auth system:

```python
from django.contrib.auth import authenticate, login, logout
```

Example:

```python
user = authenticate(request, username=username, password=password)
if user:
    login(request, user)
```


## 5. Login & Logout Views (built-in)

Handled automatically via `django.contrib.auth.views.LoginView` and `LogoutView`.

### Login view (provided by Django)

```html
<form method="post" action="{% url 'login' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
```

* **Redirect after login:**
  Add to `settings.py`:

```python
LOGIN_REDIRECT_URL = '/'  # after login
LOGOUT_REDIRECT_URL = '/'  # after logout
```

* Check authentication in template:

```django
{% if user.is_authenticated %}
  Hello, {{ user.username }}!
{% else %}
  <a href="{% url 'login' %}">Login</a>
{% endif %}
```

## 6. Signup (Custom)

Django does not provide signup by default. You need a custom view:

```python
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
```

```python
# accounts/urls.py
from django.urls import path
from .views import signup_view

urlpatterns = [
    path("signup/", signup_view, name="signup"),
]
```

### `signup.html`

```django
<h2>Sign Up</h2>
<form method="post">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Sign Up</button>
</form>
```


## 7. Redirect After Login, Logout, Signup

```python
# settings.py
LOGIN_REDIRECT_URL = "/"      # after login
LOGOUT_REDIRECT_URL = "/"     # after logout
```

For signup, just `redirect()` in your custom view.


## 8. Email Verification

Unlike **AllAuth**, Django’s built-in auth has no built-in email verification. You must:

* Send an email manually after signup.
* Or integrate with **signals** (`post_save` on `User`).

Example (console backend for testing):

```python
# settings.py
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

For easier setup, **Django AllAuth** handles email verification automatically.

## 9. Password Reset (Forgot Password)

Already included in `django.contrib.auth.urls`. Django provides built-in views for:

* Changing password (`password_change`)
* Resetting password via email (`password_reset`)

Example:

```django
<form method="post" action="{% url 'password_reset' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Reset Password</button>
</form>
```


## 10. Integrating Captcha in Login & Signup

Use `django-simple-captcha`:

```bash
pip install django-simple-captcha
```

```python
# settings.py
INSTALLED_APPS += ["captcha"]
```

```python
# urls.py
urlpatterns = [
    ...
    path("captcha/", include("captcha.urls")),
]
```

### Custom Signup Form with Captcha

```python
# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class SignupForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data["username"],
            email=self.cleaned_data["email"],
            password=self.cleaned_data["password"]
        )
        return user
```


## ✅ Summary

* Django’s built-in auth provides **login, logout, password reset, password change**.
* You must implement **signup** and **email verification** manually.
* Easy to extend with **captcha, custom forms, or signals**.


## 📚 Read More

* [How to use Django’s built-in login system](https://simpleisbetterthancomplex.com/tutorial/2016/06/27/how-to-use-djangos-built-in-login-system.html)
* [Django Login and Logout Tutorial](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
