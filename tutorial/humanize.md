# 🧑‍💻 Django Humanize Module

The **Humanize** module in Django provides **template filters** to make numbers and dates more readable for humans.


## 1. Setup

1. Add `"django.contrib.humanize"` to `INSTALLED_APPS` in **settings.py**.
2. In your template, load it with:

```django
{% load humanize %}
```


## 2. Common Filters

Here are some useful filters with simple examples:

* **`apnumber`** → Converts numbers 1–9 to words.

  ```django
  {{ 5|apnumber }}   {# → "five" #}
  ```

* **`intcomma`** → Adds commas to large numbers.

  ```django
  {{ 1234567|intcomma }}   {# → "1,234,567" #}
  ```

* **`intword`** → Converts numbers into words (millions, billions).

  ```django
  {{ 1000000|intword }}   {# → "1.0 million" #}
  ```

* **`naturalday`** → Shows natural language for dates.

  ```django
  {{ my_date|naturalday }}   {# → "yesterday" / "today" / "tomorrow" #}
  ```

* **`naturaltime`** → Relative time formatting.

  ```django
  {{ my_datetime|naturaltime }}   {# → "4 minutes ago" #}
  ```

* **`ordinal`** → Converts numbers to ordinals.

  ```django
  {{ 3|ordinal }}   {# → "3rd" #}
  ```


## 3. Read More

* [GitHub: django-humanize](https://github.com/oasiswork/django-humanize)
* [Django Docs: humanize](https://docs.djangoproject.com/en/3.2/ref/contrib/humanize/)

