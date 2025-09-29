# 🗄️ Changing Database in Django

By default, Django projects use **SQLite**. While it’s fine for development, it’s not recommended for production.
For production, you can switch to **MySQL**, **PostgreSQL**, or another robust database.


## ⚙️ Switching to MySQL

### 1. Install MySQL Client

```bash
pip install mysqlclient
```

Add it to your `requirements.txt`:

```txt
mysqlclient>=2.0
```

### 2. Update Settings

Edit `settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "your_db_name",
        "USER": "your_username",
        "PASSWORD": "your_password",
        "HOST": "localhost",   # or your DB server IP
        "PORT": "3306",        # default MySQL port
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}
```

### 3. Run Migrations

```bash
python manage.py migrate
```


## 📘 Read More

* [Django Tutorial – Databases](https://docs.djangoproject.com/en/3.2/intro/tutorial02/)
* [Django Database Reference](https://docs.djangoproject.com/en/3.2/ref/databases/)
* [DigitalOcean – Connect Django to Database](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database)
* [WebForefront – Database Setup](https://www.webforefront.com/django/setupdjangodatabase.html)


## 🔍 Database Comparisons

Choosing the right database depends on your use case:

* [Types of Modern Databases](https://www.alooma.com/blog/types-of-modern-databases)
* [Prisma Guide to Database Types](https://www.prisma.io/dataguide/intro/comparing-database-types)
