# 🐞 Django Debugging Tools

In Django, there are two common ways to debug your code:

1. **VS Code Debugger** → Set breakpoints, inspect variables, step through code.
2. **Django Debug Toolbar** → Visual in-browser panel showing SQL queries, cache usage, signals, headers, and more.

👉 Both are useful, but they serve **different purposes**:

* **VS Code Debugger** → code-level inspection.
* **Debug Toolbar** → request/response profiling and performance monitoring.


## ⚙️ Setup Django Debug Toolbar

1. Install:

   ```bash
   pip install django-debug-toolbar
   ```

2. Add to **`INSTALLED_APPS`**:

   ```python
   INSTALLED_APPS = [
       ...,
       "debug_toolbar",
   ]
   ```

3. Add to **`MIDDLEWARE`**:

   ```python
   MIDDLEWARE = [
       ...,
       "debug_toolbar.middleware.DebugToolbarMiddleware",
   ]
   ```

4. Add to **`urls.py`**:

   ```python
   import debug_toolbar
   from django.conf import settings
   from django.urls import include, path

   if settings.DEBUG:
       urlpatterns += [
           path("__debug__/", include(debug_toolbar.urls)),
       ]
   ```

5. Configure **internal IPs** (so the toolbar shows up):

   ```python
   INTERNAL_IPS = [
       "127.0.0.1",
   ]
   ```

📊 Example output:
![](/tutorial/img/debug-toolbar.png)


## 📖 Read More

* [Official Docs](https://django-debug-toolbar.readthedocs.io/en/latest/)
* [GitHub Repo](https://github.com/django-commons/django-debug-toolbar)
