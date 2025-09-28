# 🌐 Django Sites Framework

The **Sites Framework** is a built-in Django app that allows you to manage **multiple websites (domains)** from the same Django project. It’s useful when the same project powers different domains with possibly different content or behavior.


## 1. What It Does

* Keeps track of your **current domain** and **site name** in the database.
* Allows you to associate objects (like posts, pages, users, etc.) with a specific site.
* Enables multi-domain support within a single Django project.


## 2. Setup

1. Add to **`INSTALLED_APPS`** in `settings.py`:

   ```python
   INSTALLED_APPS = [
       ...
       "django.contrib.sites",
   ]
   ```

2. Define a default **`SITE_ID`** in `settings.py`:

   ```python
   SITE_ID = 1
   ```

3. Run migrations:

   ```bash
   python manage.py migrate
   ```

   This creates **two new tables**:

   * `django_site` → stores domain and name of each site.
   * Related references for site-aware apps.


## 3. Understanding `SITE_ID`

* `SITE_ID` is the **primary key** of the current site in the `django_site` table.

* Example row after migration:

  | id | domain      | name    |
  | -- | ----------- | ------- |
  | 1  | example.com | example |

* To switch between sites, simply update the value of `SITE_ID` or edit entries in the admin panel (`Sites` section).


## 4. When to Use

* Running the same Django project across **multiple domains**.
* Multi-tenant apps where content depends on the site domain.
* Projects needing **dynamic domain-based configuration**.


## 5. Read More

* [Official Docs – Sites Framework](https://docs.djangoproject.com/en/3.2/ref/contrib/sites)

