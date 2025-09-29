# ⚙️ Separating Development & Production Settings in Django

Managing different configurations for **development** and **production** is essential for security and maintainability.


## 🗂️ Project Structure

A common approach is to create a **settings package** inside your project:

```
project/
    settings/
        __init__.py
        dev.py
        prod.py
```


## 📝 Example Files

### `prod.py` (Production)

```python
from project.settings import *

# Production-specific settings
DEBUG = False
ALLOWED_HOSTS = ["example.com"]
```

### `dev.py` (Development)

```python
from project.settings import *

# Development-specific settings
DEBUG = True
ALLOWED_HOSTS = []
```


## ▶️ Running with Custom Settings

Run the server with the desired settings:

```bash
python manage.py runserver --settings=project.settings.dev
python manage.py runserver --settings=project.settings.prod
```


## 🔄 Alternative: Modify `manage.py`

You can set a **default settings file** inside `manage.py`:

```python
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.dev")
```


✅ This way, you cleanly separate environments, avoid production misconfigurations, and make deployment safer.

