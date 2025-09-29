# 🔄 Django `reverse()`

The **`reverse()` function** in Django is used to **dynamically generate URLs** from named URL patterns instead of hardcoding paths.
This makes your code more maintainable and avoids broken links if URLs change later.


## 🔹 Basic Usage

```python
from django.urls import reverse

# Simple named URL
reverse("home")  
# 👉 returns "/"

# URL with parameters
reverse("blog_detail", kwargs={"id": 5})  
# 👉 returns "/blog/5/"
```


## 🔹 Why Use `reverse()`?

✅ Avoids hardcoding URLs
✅ Keeps templates and views consistent with URL definitions
✅ Automatically adapts if URLs change


## 🔹 Usage in Views

```python
from django.http import HttpResponseRedirect
from django.urls import reverse

def my_view(request):
    return HttpResponseRedirect(reverse("home"))
```

Or more concisely with `redirect()`:

```python
from django.shortcuts import redirect

def go_to_blog(request, blog_id):
    return redirect("blog_detail", id=blog_id)
```


## 🔹 Usage in Templates

In templates, you don’t call `reverse()` directly. Instead, you use `{% url %}`:

```html
<a href="{% url 'home' %}">Home</a>
<a href="{% url 'blog_detail' id=5 %}">Blog 5</a>
```


## 🔹 Advanced Examples

```python
# Using args
reverse("article_detail", args=[2025, "django"])  
# 👉 "/articles/2025/django/"

# With namespaces
reverse("shop:product_detail", kwargs={"slug": "laptop"})  
# 👉 "/shop/products/laptop/"
```


## 🔍 Comparison: `reverse()` vs `redirect()` vs `{% url %}`

| Function/Tag     | Where to Use                        | Purpose                                                     | Example                               |
| ---------------- | ----------------------------------- | ----------------------------------------------------------- | ------------------------------------- |
| **`reverse()`**  | In Python code (views, utils, etc.) | Build a URL string from a named pattern                     | `reverse("home")  # "/home/"`         |
| **`redirect()`** | In views                            | Redirect to another view or URL (internally uses `reverse`) | `return redirect("home")`             |
| **`{% url %}`**  | In templates                        | Generate URLs dynamically in HTML                           | `<a href="{% url 'home' %}">Home</a>` |

👉 Rule of thumb:

* Use **`reverse()`** in backend logic.
* Use **`redirect()`** when sending the user to another page.
* Use **`{% url %}`** inside templates.


## ✅ Summary

* `reverse()` = build URLs in Python code
* `redirect()` = redirect users (wraps `reverse()`)
* `{% url %}` = template tag version of `reverse()`


## 📖 Read More

* [Django reverse() Docs](https://docs.djangoproject.com/en/3.2/ref/urlresolvers/#reverse)
