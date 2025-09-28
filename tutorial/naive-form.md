# 📝 Naive Form Usage in Django

While Django provides a robust **Forms framework** to handle validation, rendering, and security, it is possible to use forms in a **naive way** (directly reading request data and saving to the database). This approach is **not recommended** for production but is useful for learning the basics.


## 1. HTML Form Fields

A basic HTML form has these elements:

* `<form>`: The container element.
* `action`: The destination URL where the form data is sent.

  * ✅ Best practice: use Django’s `{% url %}` template tag.
* `method`: `GET` (default) or `POST`.
* `label`: The text describing an input.
* `input`: Collects user data.

  * `name`: The key/parameter name.
  * `type`: Type of input (`text`, `email`, `password`, etc.).
* `button`: Usually `type="submit"` to send the form.
* `csrf_token`: Protects against CSRF attacks (explained below).

### Example Form

```html
<form method="post" action="{% url 'add_post' %}">
    {% csrf_token %}
    <label for="title">Title:</label>
    <input type="text" id="title" name="title">

    <label for="content">Content:</label>
    <textarea id="content" name="content"></textarea>

    <button type="submit">Submit</button>
</form>
```


## 2. CSRF Token

### What is CSRF?

**Cross-Site Request Forgery (CSRF)** is a common security attack where a malicious site tricks a logged-in user into sending unwanted requests to another site.

### Why use it?

Django automatically protects against CSRF attacks by requiring a unique **token** in every POST form.

### How Django handles it:

* When rendering a form, add `{% csrf_token %}` inside the `<form>` tag.
* Django middleware verifies the token when the form is submitted.

```html
<form method="post">
    {% csrf_token %}
    <!-- inputs here -->
</form>
```

If you forget the CSRF token, Django will reject the request with a `403 Forbidden` error.


## 3. Naive Form Handling in Views

Here’s a simple example without using Django’s `forms` module:

```python
# views.py
from django.shortcuts import render, redirect
from .models import Post

def add_post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Post.objects.create(title=title, content=content)
        return redirect("post_list")  # after saving, redirect to post list
    return render(request, "add_post.html")
```

* `request.POST` is a dictionary containing submitted form data.
* `request.POST.get("title")` safely retrieves values.
* The data is saved directly into the model.

⚠️ **Note**: This is the simplest way, but it lacks validation, error handling, and security checks. That’s why Django’s **Forms framework** is recommended in real projects.


## 4. Displaying Data in a Template

```django
<!-- post_list.html -->
<h2>All Posts</h2>
<ul>
  {% for post in posts %}
    <li>{{ post.title }} - {{ post.content }}</li>
  {% endfor %}
</ul>
```


✅ **Summary**:

* A naive form in Django just uses raw HTML + `request.POST`.
* Always include `{% csrf_token %}` in POST forms.
* This method works for learning but should be replaced with **Django Forms** or **ModelForms** in production.


### Read More

* [Django CSRF Protection](https://docs.djangoproject.com/en/3.2/ref/csrf/)
* [Django Forms Documentation](https://docs.djangoproject.com/en/3.2/topics/forms/)

