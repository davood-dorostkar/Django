# Django ORM (Object-Relational Mapping)


## What is an ORM?

* **ORM (Object-Relational Mapping)** is a tool that connects your program to a database.
* Instead of writing raw SQL queries, you interact with the database using **Python objects and methods**.
* Django ORM works with different databases (SQLite, PostgreSQL, MySQL, etc.) without needing to change your code.

👉 **Key benefit**: If the database changes, you don’t need to rewrite everything in SQL.


## Django Admin App

Django comes with a **default admin application**, a built-in interface to manage your data.

### What it is:

* A **GUI (Graphical User Interface)** for your database.
* Allows you to **view, edit, and delete models** (database tables).
* Extremely powerful for quickly managing your project’s data.


## Creating a Superuser

By default, Django doesn’t provide an admin user.
You need to create one manually:

```bash
python manage.py createsuperuser
```

* It will ask for:

  * **Username**
  * **Email**
  * **Password**

Once created, run your server:

```bash
python manage.py runserver
```

Now, go to:

```
http://localhost:8000/admin
```

You’ll see the Django Admin login page:

![Django Admin Login](/tutorial/img/admin-login.png)


## Inside the Admin Panel

* After login, you can view all your **registered models**.
* You can **add, edit, delete** records directly from the browser.
* It’s one of Django’s most powerful features, especially in early development.


## User Model & Activation

* Every user object has an `is_active` attribute.
* This is commonly used for **email verification** or **account suspension**.
* Example:

  * `is_active = False` → User cannot log in until activation (e.g., via email link).
  * `is_active = True` → User can log in normally.


## Why Use Django ORM?

- ✅ Write queries using Python, not SQL
- ✅ Works with multiple databases (switch without rewriting code)
- ✅ Integrates tightly with Django models
- ✅ Access data through the Admin panel


## 📖 Read More

* [Django ORM Cookbook](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/)
