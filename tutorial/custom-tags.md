# Custom Template Tags

## Why Custom Template Tags?

* Not everything needs to be handled in **views**.
* Many operations can be done directly in **templates** using **custom tags** and **filters**.
* They help keep templates clean and reusable.


## Setup

1. Inside your app, create a `templatetags/` directory (at the same level as `models.py`, `views.py`, etc.).

   * Don’t forget an empty `__init__.py` file inside.

2. Create a Python file (e.g., `custom_tag.py`).

   ```py
   from django import template

   register = template.Library()
   ```

3. Load it inside your template:

   ```django
   {% load custom_tag %}
   ```


## Types of Custom Tags

### 1. Simple Tags

* Accept arguments and return a value after processing.

Example: `current_time` tag

```py
import datetime
from django import template

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)
```

**Usage:**

```django
{% current_time "%Y-%m-%d %H:%M" %}
```

### 2. Filter Tags

* Transform a value in templates.

Example with function:

```py
register.filter("snippet", snippet)
```

Example with decorator:

```py
@register.filter
def snippet(value, chars=100):
    return value[:chars] + '...'
```

**Usage in template:**

```django
{{ post.content|snippet }}
{{ post.content|snippet:300 }}
```

This works similarly to Django’s built-in `truncatechars`.


### 3. Inclusion Tags

* Return a **rendered template** with a context.
* Useful for dynamic components like “latest posts” or “category counts.”

**Example – Latest posts:**

```py
@register.inclusion_tag("latest-posts.html")
def latest_posts():
    posts = Post.objects.filter(published=True).order_by('pub_date')[:5]
    return {"posts": posts}
```

Template (`latest-posts.html`):

```django
<ul>
  {% for post in posts %}
    <li>{{ post.title }}</li>
  {% endfor %}
</ul>
```

Usage in template:

```django
{% latest_posts %}
```
>Effectively, here the latest_posts fucntion is run, then the returned value is pased to `latest-posts.html` template. Then it uses the dictionary to render the result which is put in the resulting template.

**Example – Category counts:**

```py
@register.inclusion_tag("post-categories.html")
def post_categories():
    posts = Post.objects.filter(published=True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {"categories": cat_dict}
```

**Usage in template (`post-categories.html`):**

```django
<ul>
  {% for category, count in categories.items %}
    <li>{{ category }} ({{ count }})</li>
  {% endfor %}
</ul>
```


## Read More

📖 [Django Docs – Custom Template Tags and Filters](https://docs.djangoproject.com/en/5.2/howto/custom-template-tags/)

## 📝 Some Useful Django Templates (filters and formatters)

Django templates provide **filters and template tags** to format data before rendering it on the page. This helps you display dates, times, text snippets, and handle special cases like the last item in a loop.


### 1. Using Filters with `|`

The **pipe `|`** operator applies a filter to a variable:

```django
{{ post.title|upper }}      <!-- converts to uppercase -->
{{ post.title|lower }}      <!-- converts to lowercase -->
```


### 2. Formatting Dates and Times

Django provides built-in filters to format dates and times:

```django
{{ post.published_date|date:"D M Y" }}      <!-- e.g., Fri Sep 2025 -->
{{ post.published_date|date:"d-m-Y H:i" }}  <!-- e.g., 23-09-2025 14:30 -->
{{ post.created_date|time:"H:i" }}          <!-- e.g., 14:30 -->
```

#### Read More:

* [Django Date Filter](https://docs.djangoproject.com/en/3.2/ref/templates/builtins/#date)
* [Date Filter Tutorial](https://simpleisbetterthancomplex.com/references/2016/06/21/date-filter.html)


### 3. Handling the Last Item in Loops

Sometimes you want to format items differently if they are **not the last**:

```django
{% for post in posts %}
    {{ post.title }}{% if not forloop.last %}, {% endif %}
{% endfor %}
```

* `forloop.last` is a built-in template variable that is `True` for the last item in the loop.


### 4. Text Snippets and Truncation

#### Option 1: Define a method in the model

```python
class Post(models.Model):
    content = models.TextField()

    def snippet(self):
        return self.content[:200] + '...'
```

```django
{{ post.snippet }}
```

#### Option 2: Use Django built-in template filters

```django
{{ post.content|truncatechars:200 }}   <!-- truncate after 200 characters -->
{{ post.content|truncatewords:50 }}    <!-- truncate after 50 words -->
```
