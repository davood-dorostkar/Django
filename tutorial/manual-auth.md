# ✍️ Write an Authentication App Manually

If you don’t want to use Django’s built-in auth or third-party apps, you can implement authentication manually.


## 1. Create an Authentication App

```bash
python manage.py startapp accounts
```


## 2. Add App to Settings

```python
# settings.py
INSTALLED_APPS = [
    ...
    "accounts",
]
```


## 3. Add to Project URLs

```python
# project/urls.py
from django.urls import path, include

urlpatterns = [
    ...
    path("accounts/", include("accounts.urls")),
]
```


## 4. Define App URLs

```python
# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
]
```


## 5. Create Templates

* `templates/accounts/login.html`
* `templates/accounts/signup.html`

### login.html

```html+django
<h2>Login</h2>
<form method="post">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Login</button>
</form>
```

### signup.html

```html+django
<h2>Sign Up</h2>
<form method="post">
    {% csrf_token %}
    <input type="text" name="username" placeholder="Username" required>
    <input type="email" name="email" placeholder="Email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Sign Up</button>
</form>
```


## 6. Write Views
**Login View:**
```python
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "accounts/login.html")
```
**Signup View:**
```py
from django.contrib.auth.models import User

def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            user = User.objects.create_user(username=username, email=email, password=password1)
            return redirect("login")
    return render(request, "accounts/signup.html")

```
