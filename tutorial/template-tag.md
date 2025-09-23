# Django Template Tags (using Jinja)

Django’s default template engine is **Django Template Language (DTL)**.
It’s **inspired by Jinja2**, but slightly different.

* **Jinja2** is a separate template engine (popular in Flask, can be used in Django).
* **Django Templates** include tags, filters, variables — similar syntax.

## DTL Template Syntax

* `{{ ... }}` → for **data output** (variables, expressions)
* `{% ... %}` → for **logic and functionality** (loops, conditionals, template tags)

### Example:

```django
<p>{{ username }}</p>          <!-- Displays: Alice -->
{% if items %}                <!-- Checks if list is not empty -->
    <p>You have {{ items|length }} items.</p>
{% endif %}
```

## Django Template Syntax Quick Reference

### Functions (Tags)

```django
{% if user.is_authenticated %}
    Hello, {{ user.username }}
{% endif %}

{% for post in posts %}
    <p>{{ post.title }}</p>
{% endfor %}

{% block content %}
{% endblock %}

{% include "header.html" %}
{% extends "base.html" %}
```

### Data Structures

```django
{{ title }}                <!-- simple variable -->
{{ page.title }}           <!-- object attribute -->
{{ dict.key }}             <!-- dictionary lookup -->
{{ list_items.0 }}         <!-- list index -->
{{ var.upper }}            <!-- method call -->
```

### Filters

```django
{{ name|title }}                  <!-- capitalize words -->
{{ units|lower }}                 <!-- lowercase -->
{{ post_content|truncatewords:50 }} <!-- shorten text -->
{{ order_date|date:"D M Y" }}     <!-- format date -->
{{ list_items|slice:":3" }}       <!-- slicing -->
{{ item_total|default:"nil" }}    <!-- default value -->
```