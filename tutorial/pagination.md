# Django Pagination

Pagination allows you to split large sets of data (e.g., posts, products) into multiple pages.


## Basic Usage

```py
from django.core.paginator import Paginator
posts = Post.objects.all()

# Show 2 posts per page
p = Paginator(posts, 2)

p.count        # total number of items (e.g., 4)
p.num_pages    # total number of pages (e.g., 2)
p.page_range   # iterable of page numbers -> range(1, 3)

page1 = p.page(1)
page1.object_list  # objects in page 1

page2 = p.page(2)
page2.has_next()      # False
page2.has_previous()  # True
```


## Using in Views

A common pattern: wrap in `try/except` to catch invalid page requests.

```py
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from django.http import Http404
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)  # 2 posts per page
    page_number = request.GET.get("page")

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)  # fallback to first page
    except EmptyPage:
        raise Http404("Page not found")

    return render(request, "post_list.html", {"posts": posts})
```


## Template Example

```django
<ul>
  {% for post in posts %}
    <li>{{ post.title }}</li>
  {% endfor %}
</ul>

<div class="pagination">
  {% if posts.has_previous %}
    <a href="?page={{ posts.previous_page_number }}">Previous</a>
  {% endif %}

  {% for num in posts.paginator.page_range %}
    {% if posts.number == num %}
      <strong>{{ num }}</strong>
    {% else %}
      <a href="?page={{ num }}">{{ num }}</a>
    {% endif %}
  {% endfor %}

  {% if posts.has_next %}
    <a href="?page={{ posts.next_page_number }}">Next</a>
  {% endif %}
</div>
```

This template shows:

* The list of posts.
* Page numbers with the **current page highlighted**.
* “Previous” and “Next” navigation links.


## Read More

📖 [Django Docs – Pagination](https://docs.djangoproject.com/en/5.2/topics/pagination/)

