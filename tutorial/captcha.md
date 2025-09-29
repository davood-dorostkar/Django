# 🛡️ Captcha in Django

### 🔍 What is Captcha?

Captcha (**Completely Automated Public Turing test to tell Computers and Humans Apart**) is a challenge-response system to distinguish humans from bots.

**Common types/versions:**

* **Text Captcha** → distorted text users must type.
* **Image Captcha** → select correct images (e.g., traffic lights).
* **Audio Captcha** → listen and type characters.
* **ReCAPTCHA (Google)** → invisible, checkbox, or v3 scoring system.


## ✅ Django Simple Captcha

A lightweight library to add captchas to forms.

**Setup:**

1. Install:

   ```bash
   pip install django-simple-captcha
   ```
2. Add to `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       ...,
       "captcha",
   ]
   ```
3. Add to `urls.py`:

   ```python
   path("captcha/", include("captcha.urls")),
   ```
4. Add to your **forms**:

   ```python
   from captcha.fields import CaptchaField

   class MyForm(forms.Form):
       captcha = CaptchaField()
   ```
5. Run migrations:

   ```bash
   python manage.py migrate
   ```
6. Use in template:

   ```django
   {{ form.captcha }}
   ```

📖 [Docs](https://django-simple-captcha.readthedocs.io/en/latest/usage.html)


## ✅ Django Multi Captcha Admin

Provides multiple captcha engines with Django admin integration.

**Setup:**

1. Install:

   ```bash
   pip install django-multi-captcha-admin
   ```
2. Add to `INSTALLED_APPS`:

   ```python
   INSTALLED_APPS = [
       ...,
       "django_multi_captcha_admin",
   ]
   ```
3. Set engine in `settings.py`:

   ```python
   CAPTCHA_ENGINE = "recaptcha2"  # options: recaptcha2, recaptcha3, hcaptcha, turnstile
   ```

## Read More
📖 [Docs](https://github.com/a-roomana/django-multi-captcha-admin)
