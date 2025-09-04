# 📝 Django Views – The Basics

In Django, a **view** is just a Python function (or class) that takes a web request and returns a web response.

The entry point for views is **`urls.py`**, which maps a **URL path** to a **view function**.

![](/tutorial/img/urls.jpg)

## 1. URL Configuration

* Django looks at your **project’s `settings.py`** → `ROOT_URLCONF` to know which file contains the root `urls.py`.
* Inside `urls.py`, you define **routes** that connect a URL path to a view.

📌 Example `urls.py`:

```python
from django.contrib import admin
from django.urls import path
from . import views   # import your views from the same app
# or
from project_name import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin
    path('hello/', views.http_view),  # custom view
    path('data/', views.json_view),   # custom JSON view
]
```


## 2. Writing a Simple View

A view **must** take at least one argument: `request` (an `HttpRequest` object).
It then returns an **HttpResponse** (or subclass).

### 2.1 Return an HTTP Response

```python
from django.http import HttpResponse

def http_view(request):
    return HttpResponse("Hello, Django!")
```

* Visiting `/hello/` will show `Hello, Django!` in the browser.

### 2.2 Return JSON Response

```python
from django.http import JsonResponse

def json_view(request):
    data = {
        "name": "Davood",
        "role": "Developer",
        "learning": "Django"
    }
    return JsonResponse(data)
```

* Visiting `/data/` will return JSON:

```json
{
  "name": "Davood",
  "role": "Developer",
  "learning": "Django"
}
```


## 3. How Django Handles It (Flow)

1. User enters a URL in browser → Django receives an **HTTP request**.
2. Django checks `urls.py` to see which view is mapped to that URL.
3. Django runs the matching view function.
4. The view processes the request and returns a **response** (`HttpResponse`, `JsonResponse`, etc.).
5. Django sends it back to the browser.


## 4. Visual Overview

```
Browser -----> URL (http://127.0.0.1:8000/hello/) -----> urls.py -----> views.py -----> Response
```