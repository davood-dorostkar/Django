# 🔑 Django AllAuth Module

`django-allauth` is a powerful authentication package for handling **login, logout, signup, email verification, password management, and third-party logins**.


## 1. Setup Package

Install and configure AllAuth:

```bash
pip install django-allauth
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    "django.contrib.sites",   # required
    "allauth",
    "allauth.account",
    "allauth.socialaccount",  # optional (social logins)
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",  # default
    "allauth.account.auth_backends.AuthenticationBackend",
]

# AllAuth settings
LOGIN_REDIRECT_URL = "/"   # redirect after login
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
```

```python
# project/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path("accounts/", include("allauth.urls")),
]
```


## 2. Login and Logout

AllAuth provides ready-made views:

```html+django
<!-- login.html -->
<h2>Login</h2>
<form method="post" action="{% url 'account_login' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>

<a href="{% url 'account_logout' %}">Logout</a>
```


## 3. Signup

```html+django
<!-- signup.html -->
<h2>Sign Up</h2>
<form method="post" action="{% url 'account_signup' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
</form>
```


## 4. Email Verification

* After signup, AllAuth sends a verification email.
* You must configure email backend:

```python
# settings.py
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# For production, configure SMTP
```

Users get an email with a confirmation link.


## 5. Password Reset (Forgot Password)

AllAuth includes password reset views:

```html+django
<!-- password_reset.html -->
<h2>Forgot Password?</h2>
<form method="post" action="{% url 'account_reset_password' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Reset</button>
</form>
```

✅ This will send a reset link to the user’s email.


## 6. Integrating Captcha

Install `django-simple-captcha`:

```bash
pip install django-simple-captcha
```

```python
# settings.py
INSTALLED_APPS += ["captcha"]
```

```python
# urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path("captcha/", include("captcha.urls")),
]
```

Extend the **signup form** to include captcha:

```python
# accounts/forms.py
from allauth.account.forms import SignupForm
from captcha.fields import CaptchaField

class CustomSignupForm(SignupForm):
    captcha = CaptchaField()

    def save(self, request):
        user = super().save(request)
        return user
```

```python
# settings.py
ACCOUNT_FORMS = {
    "signup": "accounts.forms.CustomSignupForm",
}
```

Now the signup page will display a captcha.


## 7. Other Features (etc.)

* **Social logins** (Google, GitHub, Facebook, etc.) via `allauth.socialaccount`.
* **Custom redirect after login/logout** with `LOGIN_REDIRECT_URL` and `ACCOUNT_SIGNUP_REDIRECT_URL`.
* **Custom email templates** by overriding:

  * `account/email/email_confirmation_message.txt`
  * `account/email/password_reset_key_message.txt`
