# 🚀 Deploy on Cloud (Liara)

Liara provides a **PaaS (Platform-as-a-Service)** environment for deploying Django applications with integrated database and storage options.


## ⚙️ Services You Need

To deploy your Django app, you typically need to create:

* **Platform** → Your backend service (Django app).
* **Database** → PostgreSQL, MySQL, etc.
* **Disks** → For static and media files. Even if your platform disk is large enough, separating storage is recommended.


## 📄 Liara Configuration (`liara.json`)

Liara supports a `liara.json` file placed beside `manage.py`. It manages resources and deployment automatically.

**Example:**

```json
{
  "platform": "django",
  "django": {
    "python_version": "3.10",
    "collectstatic": true,
    "timezone": "UTC"
  },
  "app": {},
  "disks": {}
}
```


## 📤 Uploading Code

You can deploy your project to Liara using:

* **Liara GUI** (dashboard upload)
* **Liara CLI** (recommended for automation)

⚠️ **Note:** Liara’s terminal does not allow running `makemigrations`.

* Run `python manage.py makemigrations` locally.
* Upload migration files with your code.
* On the server, only run `python manage.py migrate`.


## 🔑 Handling Environment Variables with `python-decouple`

Use [python-decouple](https://github.com/henriquebastos/python-decouple) to manage environment variables securely.

### Setup

1. Install the package:

   ```bash
   pip install python-decouple
   ```
2. Create a `.env` file beside `manage.py`:

   ```ini
   DEBUG=True
   SECRET_KEY=xxxxx
   ```
3. Load values in `settings.py`:

   ```python
   from decouple import config

   DEBUG = config("DEBUG", default=False, cast=bool)
   SECRET_KEY = config("SECRET_KEY")
   ```

### Advanced Example

```python
DATABASES = {
    'default': {
        'ENGINE': config("DB_ENGINE", default="django.db.backends.sqlite3"),
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

* Values can be defined either in `.env` or directly in Liara’s **Dashboard → Environment Variables**.
* Update values (e.g., DB credentials, network configs) based on your services in Liara.


## 🌐 Nginx 

Liara uses **Nginx** to:

* Serve **static** and **media files**
* Route requests to the correct service
* Handle **Gzip compression** for performance
* Manage **HTTP headers**
* Enable **SSL and HTTPS**
