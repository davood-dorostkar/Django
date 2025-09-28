# ⚡ Django Extensions

**Django Extensions** is a popular third-party app that adds **extra management commands** and utilities to Django’s `manage.py`. It is especially useful for debugging, visualization, and rapid development.


## 1. Installation

1. Install via pip:

   ```bash
   pip install django-extensions
   ```
2. Add to **settings.py**:

   ```python
   INSTALLED_APPS = [
       ...
       "django_extensions",
   ]
   ```


## 2. Usage Examples

After setup, you can use many extra `manage.py` commands:

* **`graph_models`** → Generates a visual diagram of your models.

  ```bash
  python manage.py graph_models -a -o my_models.png
  ```

* **`show_urls`** → Lists all registered URLs in your project.

  ```bash
  python manage.py show_urls
  ```

* **`validate_templates`** → Checks templates for syntax errors.

  ```bash
  python manage.py validate_templates
  ```

* **`shell_plus`** → An improved shell with automatic model imports.

  ```bash
  python manage.py shell_plus
  ```

* **Other useful commands**:

  * `runscript` → Run custom Python scripts inside Django.
  * `sqldiff` → Compare database schema vs. Django models.
  * `create_command` → Scaffold new custom commands quickly.


## 3. Read More

* [GitHub: django-extensions](https://github.com/django-extensions/django-extensions)
* [Official Docs](https://django-extensions.readthedocs.io/en/latest)
