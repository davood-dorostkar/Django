# Dynamic URLs
## Dynamic URLs with Parameters

You can pass parameters to views using the URL pattern.

**Example (single parameter):**

```python
# urls.py
path('posts/<int:id>/', views.post_detail, name='post_detail')

# views.py
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, "post_detail.html", {"post": post})
```

**Example (multiple parameters with static text):**

```python
path('blog/<int:year>/<slug:slug>/', views.post_archive, name='post_archive')
```

📖 [Read more](https://docs.djangoproject.com/en/3.2/topics/http/urls/)