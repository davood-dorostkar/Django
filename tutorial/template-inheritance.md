# Django Template Inheritance

Django’s template inheritance system lets you **reuse common structures** (like headers, footers, navigation bars) across multiple pages, while customizing only the parts that change.

It works similarly to object-oriented inheritance — a **base template** defines the general structure, and **child templates** override specific sections.


## Defining Blocks in a Parent Template

A **block** is a placeholder that child templates can override.

Example: `base.html`

```django
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{% block title %}My Website{% endblock title %}</title>
    {% block head %}{% endblock head %}
</head>
<body>
    <header>
        {% include "header.html" %}
    </header>

    <main>
        {% block content %}{% endblock content %}
    </main>

    <footer>
        {% include "footer.html" %}
    </footer>

    {% block scripts %}{% endblock scripts %}
</body>
</html>
```

Here, we defined **blocks**:

* `title` → for page titles
* `head` → for custom `<meta>`, CSS, etc.
* `content` → main content area
* `scripts` → custom JavaScript per page

>The block name in `endblock` is optional (`{% endblock }`)

## Extending a Parent Template

A child template can **extend** the base template and override its blocks.

Example: `home.html`

```django
{% extends "base.html" %}

{% block title %}Home - My Website{% endblock title %}

{% block content %}
<h1>Welcome to the homepage!</h1>
<p>This content is unique to the home page.</p>
{% endblock content %}

{% block scripts %}
<script src="{% static 'js/home.js' %}"></script>
{% endblock scripts %}
```

* The page still includes `header.html` and `footer.html`
* Only the `content`, `title`, and `scripts` blocks were customized


## Reusing a Block in a Child Template

If you want to keep **the parent block content** but add something extra, use `{{ block.super }}`.

Example:

```django
{% block head %}
    {{ block.super }}
    <link rel="stylesheet" href="{% static 'css/custom.css' %}">
{% endblock head %}
```

This keeps whatever was inside `head` in the parent and adds new CSS.


## Including Other Templates

### What is `include`?

* `extends` → defines a **base template** that child templates build upon.
* `include` → inserts a **module (partial template)** into another template.

This is useful for repeating components like ads, navigation bars, or footers.

`{% include %}` inserts another template file directly. Useful for **repeated components** like headers, navbars, or sidebars.

### Example

**ads.html**

```html
<div class="ad-banner">
    <img src="{% static 'images/ad.png' %}" alt="Advertisement">
</div>
```

**base.html**

```html
{% load static %}
<html>
  <body>
    <h1>My Website</h1>
    {% include 'ads.html' %}
  </body>
</html>
```

### Notes

* Always use `{% load static %}` in both the **included file** and the **including file** if static files are used.
* `include` does not inherit blocks; it just injects the content as-is.


## Important Note: Loading Static Files

👉 **`{% load static %}` must be written in each template file where you use `{% static %}`.**
It is **not inherited** automatically.

Example:

```django
{% load static %}
<img src="{% static 'images/logo.png' %}" alt="Logo">
```


## Best Practices

✅ Create a **base template** (e.g., `base.html`) with:

* `<head>` (CSS links, meta tags, etc.)
* `<header>` (logo, navbar, etc.)
* `<footer>` (common footer info)
* `<script>` tags

✅ Use `{% extends "base.html" %}` in **all child templates**.
✅ Keep **small, reusable components** (`header.html`, `footer.html`, `navbar.html`) in `templates/includes/` and load them with `{% include %}`.
✅ Use `{{ block.super }}` if you want to append to a parent block.
✅ Always `{% load static %}` in files where you use `{% static %}`.


## Example: Full Setup

### base.html

```django
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Default Title{% endblock title %}</title>
    <link rel="stylesheet" href="{% static 'css/base.css' %}">
    {% block head %}{% endblock head %}
</head>
<body>
    {% include "includes/navbar.html" %}
    <main>
        {% block content %}{% endblock content %}
    </main>
    {% include "includes/footer.html" %}
    {% block scripts %}{% endblock scripts %}
</body>
</html>
```

### home.html

```django
{% extends "base.html" %}
{% load static %}

{% block title %}Home Page{% endblock title %}

{% block content %}
<h1>Welcome!</h1>
<img src="{% static 'images/banner.png' %}" alt="Banner">
{% endblock content %}

{% block scripts %}
<script src="{% static 'js/home.js' %}"></script>
{% endblock scripts %}
```


✅ This structure ensures consistency across your site while letting each page stay flexible.
