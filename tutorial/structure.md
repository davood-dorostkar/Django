# 🏗️ Django Project Structure

When you run:

```sh
python manage.py
```

Django shows all available commands (like `runserver`, `migrate`, `createsuperuser`, etc.).
To use Django effectively, it’s important to understand the **key files** and **architecture**.


## 1. Important Files in a Django Project

| File              | Purpose                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **`manage.py`**   | Command-line utility. Used to run the server, apply migrations, create apps, etc. (e.g., `python manage.py runserver`). |
| **`__init__.py`** | Marks a directory as a Python package. Without it, Python won’t recognize the folder as importable.                     |
| **`settings.py`** | The main configuration file: database settings, installed apps, middleware, templates, security, etc.                   |
| **`urls.py`**     | Maps URL patterns to views. Acts like a “table of contents” for the project’s routes.                                   |
| **`wsgi.py`**     | Entry point for **WSGI servers** (e.g., Gunicorn, uWSGI). Used in deployment for handling requests.                     |
| **`asgi.py`**     | Entry point for **ASGI servers** (e.g., Daphne, Uvicorn). Supports asynchronous requests (WebSockets, long polling).    |


## 2. Key Sections in `settings.py`

These are the most important configuration variables:

* **`BASE_DIR`** → Path to the project’s root directory. Helps reference files (e.g., templates, static files).
* **`SECRET_KEY`** → Used for cryptographic signing (must be kept secret in production!).
* **`ALLOWED_HOSTS`** → A list of host/domain names that the app can serve (e.g., `['localhost', 'example.com']`).
* **`INSTALLED_APPS`** → A list of active Django and third-party apps used in the project (e.g., `django.contrib.admin`, `rest_framework`).
* **`MIDDLEWARE`** → Functions that process requests/responses before reaching views (e.g., authentication, security, sessions).
* **`ROOT_URLCONF`** → The Python path to the root `urls.py` file. Django uses it to find URL patterns.
* **`TEMPLATES`** → Settings for template engines (default: Django’s template engine). Defines where `.html` files live.
* **`WSGI_APPLICATION`** → Path to the WSGI application (links `wsgi.py`). Required for deployment on WSGI servers.
* **`AUTH_PASSWORD_VALIDATORS`** → Security rules for passwords (e.g., minimum length, complexity).
* **`STATIC_URL`** → Base URL for serving static files (e.g., CSS, JavaScript, images).


## 3. Django Architecture

Django is based on a design pattern similar to **MVC (Model-View-Controller)**, but with its own twist called **MVT (Model-View-Template)**.


### 🔹 MVC (Model-View-Controller)

* **Model** → Manages data and business logic.
* **View** → Defines how data is presented (UI).
* **Controller** → Handles user input, updates Model, and refreshes View.

📌 Example: In a blog app,

* Model = `Post` class (title, content, date)
* View = HTML page displaying posts
* Controller = Function that saves posts and reloads the page


### 🔹 MVT (Model-View-Template) in Django

* **Model** → Same as MVC. Defines data (tables) and how to interact with it.
* **View** → Functions or classes in Django (`views.py`). Handle user input, query models, and return a response. (In Django, this acts more like the **Controller** in MVC.)
* **Template** → Defines **presentation** (HTML, CSS, UI). Django uses its template engine (`.html` files with template tags).

📌 Example in Django:

* Model → `Post` model in `models.py`
* View → `post_list` function in `views.py`
* Template → `post_list.html`

So:
👉 In Django, the **View ≈ Controller**, and the **Template = View layer in MVC**.


### 📸 Diagram: MVT Flow

![](/tutorial/img/mvt.jpg)


## 4. Read More

* [ASGI Introduction](https://florimond.dev/en/posts/2019/08/introduction-to-asgi-async-python-web/)