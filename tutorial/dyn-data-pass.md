# Passing Dynamic Data to Templates

Django lets you send data from your **views** (Python code) into your **templates** (HTML files).
This is done using the **`context`** parameter in the `render()` function.


## Using `context` in Views

The `render()` function takes three arguments:

1. `request` → the HTTP request object
2. `template_name` → which HTML template to render
3. `context` → a dictionary containing dynamic data

### Example View

```python
from django.shortcuts import render

def home(request):
    context = {
        "title": "Welcome Page",
        "username": "Alice",
        "items": ["Book", "Laptop", "Phone"]
    }
    return render(request, "home.html", context)
```

Here we pass three keys: `title`, `username`, and `items`.


## Accessing Data in Templates

Inside the template (`home.html`), use **double curly braces** `{{ }}` to insert variables.

### Example Template

```django
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Hello, {{ username }}!</h1>
    <p>Here is your item list:</p>

    <ul>
        {% for item in items %}
            <li>{{ item }}</li>
        {% endfor %}
    </ul>
</body>
</html>
```

## Full Workflow

1. **Browser requests page** → `/`
2. **Django view** runs and prepares `context` data
3. **Template** receives the dictionary
4. Variables inside `{{ }}` are replaced with actual values
5. Final HTML is sent to the browser
