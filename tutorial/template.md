# Django Templates

In Django, **templates** are HTML files (or other text formats) used to generate the user-facing pages.
Views are responsible for the logic, while templates handle the presentation.

This follows Django’s **MTV pattern** (Model–Template–View):

* **Model** → data
* **Template** → presentation (HTML)
* **View** → business logic, combines models and templates


## Template Configuration in `settings.py`

Django looks at the `TEMPLATES` setting in `settings.py` to know where and how to find templates:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],       # list of extra directories to search for templates
        'APP_DIRS': True, # auto-search 'templates' folder inside installed apps
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

### Key Points:

* **`DIRS`** → a list of extra directories where Django should look for templates (e.g., a global `templates/` folder).
* **`APP_DIRS`** → if `True`, Django will automatically look for a `templates/` directory inside each app in `INSTALLED_APPS`.
* **`context_processors`** → functions that inject extra variables into every template (e.g., `request`, `user`, `messages`).


## Where to Put Templates

1. **App-specific templates**
   Each app can have its own `templates/` folder:

   ```
   blog/
       templates/
           blog/
               index.html
               post_detail.html
   ```

   ✅ Namespacing (having a `blog/` subfolder) is recommended to avoid conflicts across apps.

2. **Global templates**
   You can also have a global `templates/` directory in your project root:

   ```
   project/
       templates/
           base.html
           home.html
   ```

   Then add it to `DIRS` in `settings.py`:

   ```python
   'DIRS': [BASE_DIR / "templates"],
   ```


## Rendering Templates in Views

To return an HTML response from a view, use **`render()`**:

```python
from django.shortcuts import render

def main_view(request):
    return render(request, 'main.html')
```

* `render(request, template_name, context={})` is a shortcut for creating an `HttpResponse`.
* The second argument is the **template file name** (Django searches based on `TEMPLATES` settings).
* The optional `context` argument is a dictionary of variables passed to the template.

Example with context:

```python
def hello_view(request):
    return render(request, 'hello.html', {"name": "Davood"})
```

In `hello.html`:

```html
<h1>Hello, {{ name }}!</h1>
```

Result: **Hello, Davood!**


## Template Inheritance (Best Practice)

Django supports **template inheritance** to avoid repeating common HTML.

`base.html` (layout):

```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My Site{% endblock %}</title>
</head>
<body>
    <header>My Website Header</header>
    <main>
        {% block content %}{% endblock %}
    </main>
    <footer>Footer</footer>
</body>
</html>
```

`home.html` (extends base):

```html
{% extends "base.html" %}

{% block title %}Home Page{% endblock %}

{% block content %}
<h1>Welcome to the Home Page</h1>
{% endblock %}
```

This makes maintenance easier across multiple pages.


## Using Django Settings in Views

Sometimes you need access to project settings inside your views.

### Proper Usage Examples

**Correct way:**
```python
from django.conf import settings

def my_view(request):
    media_root = settings.MEDIA_ROOT
    base_dir = settings.BASE_DIR
    debug_mode = settings.DEBUG
```

**Also correct** (for frequently used settings):
```python
from django.conf import settings

BASE_DIR = settings.BASE_DIR
DEBUG = settings.DEBUG
```

### Key Differences

| Aspect | `from project import settings` | `from django.conf import settings` |
|--------|--------------------------------|-------------------------------------|
| **Circular imports** | High risk | No risk |
| **Environment support** | Poor (hardcoded) | Excellent |
| **Default values** | Doesn't use Django defaults | Uses Django defaults |
| **Best practice** | ❌ Not recommended | ✅ Recommended |
| **Testing** | Problems with test settings | Works with test settings |

## Summary

* Templates define how your views’ data is displayed to users.
* Configured in the `TEMPLATES` setting (`DIRS`, `APP_DIRS`, `context_processors`).
* Place templates inside app folders (`app/templates/app_name/...`) or in a global `templates/` folder.
* Use `render(request, template, context)` to return HTML.
* Pass data via context dictionaries.
* Use template inheritance (`{% extends %}`, `{% block %}`) for DRY code.
* Access project settings via `from django.conf import settings`.


