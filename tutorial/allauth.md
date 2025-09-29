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

# AllAuth optional configurations
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = "username_email"
LOGIN_REDIRECT_URL = "/"   # redirect after login
LOGOUT_REDIRECT_URL = "/"
```
### urls.py
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

* **Login URL:** `/accounts/login/`
* **Logout URL:** `/accounts/logout/`

Template snippet for login (optional if you use default AllAuth template):

```django
<form method="post" action="{% url 'account_login' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Login</button>
</form>
```


## 3. Signup
* **Signup URL:** `/accounts/signup/`
* **Email verification** can be enabled via `ACCOUNT_EMAIL_VERIFICATION = "mandatory"`
* Users receive a verification email to activate their account.

```django
<!-- signup.html -->

<form method="post" action="{% url 'account_signup' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Sign Up</button>
</form>
```


## 4. Email Verification

AllAuth handles email verification automatically:

* Email is sent on signup.
* User cannot login until the email is verified (if `mandatory` is set).
* You can customize the email templates in `templates/account/email/`.
* You must configure email backend:

```python
# settings.py
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
# For production, configure SMTP
```

Users get an email with a confirmation link.


## 5. Password Reset (Forgot Password)

* **Password reset URL:** `/accounts/password/reset/`
* Django AllAuth provides the full workflow:

  * request reset → email with token → enter new password.

Example template usage:

```django
<form method="post" action="{% url 'account_reset_password' %}">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Reset Password</button>
</form>
```


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
Then add to settings:
```python
# settings.py
ACCOUNT_FORMS = {
    "signup": "accounts.forms.CustomSignupForm",
}
```

Now the signup page will display a captcha.


## 7. Social Authentication (Optional)

You can integrate social login providers like Google, Facebook, GitHub:

```python
INSTALLED_APPS += [
    "allauth.socialaccount.providers.google",
]

# Then configure client id and secret in admin
```


## 8. Templates

AllAuth provides default templates. You can override by creating:

```
templates/account/login.html
templates/account/signup.html
templates/account/email/email_confirmation_message.txt
```


## 9. Additional Settings and Customization

* `ACCOUNT_USERNAME_REQUIRED = False` → if you want signup via email only
* `ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True/False`
* Customize redirects with `LOGIN_REDIRECT_URL` and `LOGOUT_REDIRECT_URL`


## Read More

* [Django AllAuth Documentation](https://django-allauth.readthedocs.io/en/latest/)
* [Django AllAuth GitHub](https://github.com/pennersr/django-allauth)