# Django Authentication System

Django provides a powerful built-in authentication framework.
By default, **auth-related tables are created automatically** and the system uses the **User model** internally.

There are three main ways to implement authentication (explained in later sections):

* [Manual authentication app](/tutorial/manual-auth.md)
* [Third-Party apps (AllAuth)](/tutorial/allauth.md)
* [Django built-in `auth` app](/tutorial/contrib-auth.md)

> ✅ Choose based on project needs.
>
> * Manual → full control.
> * AllAuth → flexible, supports social login.
> * Built-in → simple username/password auth.


## Checking Authentication Status

* **In views**: `if request.user.is_authenticated: ...`
* **In templates**: `{% if user.is_authenticated %}...{% endif %}`

```python
# views.py
def profile(request):
    if request.user.is_authenticated:
        return render(request, "profile.html")
    return redirect("login")
```


## `authenticate()`, `login()`, `logout()`

* `authenticate()` → verifies credentials and returns a `User` object.
* `login()` → attaches user to session.
* `logout()` → removes user session.

```python
from django.contrib.auth import authenticate, login, logout

user = authenticate(request, username="john", password="secret")
if user:
    login(request, user)  # user logged in
else:
    print("Invalid credentials")

logout(request)  # logs out user
```


## Authentication with Forms

### Using `AuthenticationForm`

```python
from django.contrib.auth.forms import AuthenticationForm
form = AuthenticationForm(data=request.POST)
```

Custom form (inheriting `AuthenticationForm`):

```python
from django.contrib.auth.forms import AuthenticationForm

class CustomAuthForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        if not user.is_active:
            raise forms.ValidationError("Inactive account")
```


### Using `UserCreationForm`

```python
from django.contrib.auth.forms import UserCreationForm
form = UserCreationForm(request.POST)
```

Custom form:

```python
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ("username", "email")
```

#### `password1` and `password2`

* `password1` = password input
* `password2` = confirm password

```python
# signup form ensures both match
```


## Pre-Filling Forms for Authenticated Users

You can pre-populate forms for logged-in users with hidden fields.

```django
<form method="post" action="{% url 'comments:post' post.id %}">
    {% csrf_token %}

    {% if request.user.is_authenticated %}
        <input type="hidden" name="name" value="{{ request.user.username }}">
        <input type="hidden" name="email" value="{{ request.user.email }}">
    {% else %}
        <input type="text" name="name" placeholder="Name" required>
        <input type="email" name="email" placeholder="email@example.com" required>
    {% endif %}

    <textarea name="message" placeholder="Your message..." required></textarea>

    <button type="submit">Post Comment</button>
</form>

```

## Read More

* [Django Docs: Authentication](https://docs.djangoproject.com/en/3.2/topics/auth/default/)
* [MDN: Django Authentication](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Authentication)
* [Dev.to Guide](https://dev.to/sm0ke/django-authentication-system-4ha9)
* [Auth0 Blog](https://auth0.com/blog/django-authentication/)
