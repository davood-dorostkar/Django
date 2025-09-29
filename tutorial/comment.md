# 💬 Commenting in Django

There are two main ways to add comments to your Django project:


## 🔹 Using Disqus (Third-Party Service)

1. Register at [Disqus](https://disqus.com/).
2. Copy the **embed code snippet** they provide.
3. Paste the snippet into your Django **template** where you want comments to appear.

✅ Advantages: Easy setup, built-in moderation & spam filtering.
⚠️ Limitation: Comments are stored outside your database (on Disqus servers).


## 🔹 Creating a Simple Commenting System (Manual)

If you want **full control**, you can build your own commenting feature.

### 1. Create a `Comment` Model

```python
# models.py
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):  # Example Post model
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
```


### 2. Register in Admin

```python
# admin.py
from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
```


### 3. Create a Form for Comments

```python
# forms.py
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
```


### 4. Handle Comments in Views

```python
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import CommentForm

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_detail", post_id=post.id)
    else:
        form = CommentForm()

    return render(request, "post_detail.html", {"post": post, "comments": comments, "form": form})
```


### 5. Template Example

```html
<!-- post_detail.html -->
<h1>{{ post.title }}</h1>
<p>{{ post.content }}</p>

<hr>
<h2>Comments</h2>
{% for comment in comments %}
  <p><b>{{ comment.author }}</b>: {{ comment.content }} <i>({{ comment.created_at }})</i></p>
{% empty %}
  <p>No comments yet.</p>
{% endfor %}

<hr>
<h2>Add a Comment</h2>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```


✅ Advantages: Integrated with your database, full customization.
⚠️ Limitation: Requires implementing moderation & spam protection manually.

