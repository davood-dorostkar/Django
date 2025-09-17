# MakeMigration & Migrate

Working with data in Django involves **databases (DB)**.
At the core, databases use **SQL (Structured Query Language)** to **store, retrieve, and manipulate data**.


## What is SQL?

* **SQL (Structured Query Language)** → a language to interact with databases.
* Used to **define tables**, **insert records**, **query data**, and **update/delete entries**.


## CRUD Operations

Almost everything you do with a database falls into these 4 actions:

1. **C → Create** (add new data)
2. **R → Retrieve** (read data)
3. **U → Update** (modify existing data)
4. **D → Delete** (remove data)

![Database CRUD illustration](/tutorial/img/db.png)


## Django and Migrations

Django provides a **migration system** to translate your Python models into SQL queries automatically.

### 1. `makemigrations`

* Tells Django: “Look at my models and prepare the database changes.”
* Creates a list of SQL queries (but doesn’t run them yet).
* Stores these in a **`migrations/` directory** inside each app.

Command:

```bash
python manage.py makemigrations
```

Example output:

```
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Post
```


### 2. `migrate`

* Actually **applies the SQL queries** to the database.
* Updates your database schema to match your models.

Command:

```bash
python manage.py migrate
```

Example output:

```
Applying blog.0001_initial... OK
```


## Default Database

* By default, Django uses **SQLite3**, a lightweight file-based database.
* File is usually located at `db.sqlite3` in your project root.

👉 To explore your SQLite database, you can use **DB Browser for SQLite** (a GUI tool).


## Typical Workflow

1. Define or update models in `models.py`
2. Run:

   ```bash
   python manage.py makemigrations
   ```

   → generates migration files
3. Run:

   ```bash
   python manage.py migrate
   ```

   → applies changes to database


## Example

### Model (`models.py`)

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
```

### Commands

```bash
python manage.py makemigrations
python manage.py migrate
```

### Result

* Django creates a `books` table in your SQLite database with `title` and `author` columns.


## Summary

* **`makemigrations`** → prepares SQL queries based on model changes
* **`migrate`** → runs those queries to update the database
* Together, they keep your **Python models** and **database schema** in sync


## 📖 Read More

🔗 [Django Documentation on Migrations](https://docs.djangoproject.com/en/3.2/topics/migrations/)
