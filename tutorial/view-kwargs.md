# Dynamic Views in Django

When building web applications, you often need flexible views that can handle **multiple URLs**, **optional parameters**, or **dynamic data**. Django provides tools like `kwargs` and default arguments to make your views robust and reusable.


## 1. Using a Single View for Multiple URLs

Instead of creating separate views for each URL, you can point multiple URLs to the **same view** and use optional parameters to customize behavior.

### Example

```python
# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blog_view, name='blog_home'),
    path('blog/category/<str:category>/', views.blog_view, name='blog_category'),
]
```

In the view, you can define a **default value** for the parameter:

```python
# views.py
from django.shortcuts import render
from blog.models import Post

def blog_view(request, category=None):
    if category:
        posts = Post.objects.filter(category__name=category)
    else:
        posts = Post.objects.all()
    return render(request, 'blog.html', {'posts': posts})
```

✅ This approach lets you:

* Serve all posts at `/blog/`
* Filter posts by category at `/blog/category/<name>/`
* Avoid code duplication and keep views DRY (Don't Repeat Yourself)


## 2. Using `kwargs` for Multiple Inputs

`**kwargs` is a flexible way to handle **dynamic URL parameters** in a view.

* Captures all keyword arguments as a dictionary
* Useful when your URL has multiple optional or dynamic parts

### Example

```python
# urls.py
urlpatterns = [
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('users/<str:username>/profile/', views.user_profile, name='user_profile'),
]
```

```python
# views.py
from django.shortcuts import get_object_or_404
from blog.models import Post
from django.http import HttpResponse

def post_detail(request, **kwargs):
    post_id = kwargs.get('post_id')  # returns None if not present
    post = get_object_or_404(Post, id=post_id)
    return HttpResponse(f"Post title: {post.title}")

def user_profile(request, **kwargs):
    username = kwargs.get('username')
    return HttpResponse(f"Profile page of {username}")
```


## 3. Handling Non-Existent Inputs

Using `.get()` ensures your code doesn’t break if a parameter is missing:

```python
def my_view(request, **kwargs):
    value = kwargs.get('some_key')  # returns None if key doesn't exist
    if value:
        return HttpResponse(f"Value is: {value}")
    return HttpResponse("No value provided")
```


## 4. Combining `kwargs` with URL Parameters

For URLs with multiple parameters:

```python
path('posts/<int:post_id>/comments/<int:comment_id>/', views.comment_detail, name='comment_detail')
```

```python
def comment_detail(request, **kwargs):
    post_id = kwargs.get('post_id')
    comment_id = kwargs.get('comment_id')
    return HttpResponse(f"Post {post_id}, Comment {comment_id}")
```


## ✅ Summary

* A single view can handle multiple URLs using optional parameters.
* Use `kwargs` to capture multiple dynamic inputs in views.
* Always use `.get('key')` to safely access parameters and avoid errors.
* This makes your Django views **flexible, reusable, and robust**.
