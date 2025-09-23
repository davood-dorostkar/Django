# 🌐 HTTP Basics 

The **HyperText Transfer Protocol (HTTP)** is the foundation of communication on the web. Every time your Django app interacts with a browser, it’s through HTTP requests and responses.


## 1. HTTP Methods

HTTP defines different **methods** that tell the server what action the client wants to perform.

| Method     | Purpose                                                                                                       | Django Example                              |
| ---------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **GET**    | Retrieve data from the server. Parameters are visible in the URL.                                             | A blog page request (`/posts/5/`).          |
| **POST**   | Submit data to the server (form submission, file upload). Parameters are in the body, not visible in the URL. | User login form.                            |
| **PUT**    | Update/replace an entire resource.                                                                            | API replacing a blog post.                  |
| **PATCH**  | Update only part of a resource.                                                                               | API changing just the title of a blog post. |
| **DELETE** | Remove a resource.                                                                                            | API deleting a blog post.                   |

📌 Example in Django (`views.py`):

```python
from django.http import HttpResponse

def handle_request(request):
    if request.method == "GET":
        return HttpResponse("This is a GET request")
    elif request.method == "POST":
        return HttpResponse("This is a POST request")
```

👉 In Django REST Framework (DRF), you’ll see these methods used a lot when building APIs.


## 2. HTTP Response Codes

When Django (or any server) responds, it sends back a **status code**.
Here are the most common categories:

* **2xx – Success**

  * `200 OK` → Request succeeded.
  * `201 Created` → New resource created (common with POST).

* **3xx – Redirection**

  * `301 Moved Permanently` → Resource has a new URL.
  * `302 Found` → Temporary redirect.

* **4xx – Client Errors**

  * `400 Bad Request` → Invalid request.
  * `401 Unauthorized` → Authentication required.
  * `403 Forbidden` → Permission denied.
  * `404 Not Found` → Resource doesn’t exist.

* **5xx – Server Errors**

  * `500 Internal Server Error` → Something broke on the server.
  * `502 Bad Gateway`, `503 Service Unavailable` → Server issues.

📌 Example in Django:

```python
from django.http import HttpResponseNotFound

def page_not_found(request):
    return HttpResponseNotFound("Oops! Page not found.")
```

## 3. HTTP Methods in Django

In web applications, HTTP methods define the type of action a client wants to perform on a server. Django allows you to handle these methods easily in your views.


### 3.1. Request Method Overview

Every request sent to a Django view contains the HTTP method. You can check the method in your view:

```python
# views.py
from django.http import HttpResponse

def my_view(request):
    if request.method == "GET":
        return HttpResponse("This is a GET request.")
    elif request.method == "POST":
        return HttpResponse("This is a POST request.")
```

### 3.2. GET Method

* Data sent with **GET** is appended to the URL:

```
/search/?q=django
```
* In Django, you can access it via `request.GET`:

```python
def search_view(request):
    query = request.GET.get("q")  # returns None if 'q' not in GET
    return HttpResponse(f"You searched for: {query}")
```


### 3.3. POST Method

* Used to send data securely to the server (e.g., forms).
* Data is accessed via `request.POST`:

```python
def submit_form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Hello, {name}!")
    return HttpResponse("Please submit the form.")
```


### 3.4. Sending Data in URLs (GET Example)

```html
<form method="get" action="/search/">
    <input type="text" name="q" placeholder="Search">
    <button type="submit">Search</button>
</form>
```

* When submitted, the browser navigates to `/search/?q=value`.
* `request.GET` will contain `{'q': 'value'}`.


### 3.5. Common HTTP Responses in Django

Django provides several helper classes for common HTTP responses:

| Response Class                  | Purpose                            |
| ------------------------------- | ---------------------------------- |
| `HttpResponse`                  | Standard 200 OK response           |
| `HttpResponseNotFound`          | 404 Not Found                      |
| `HttpResponseRedirect`          | Redirect to another URL (302)      |
| `HttpResponsePermanentRedirect` | Permanent redirect (301)           |
| `HttpResponseForbidden`         | 403 Forbidden                      |
| `HttpResponseBadRequest`        | 400 Bad Request                    |
| `HttpResponseServerError`       | 500 Internal Server Error          |
| `Http404`                       | Raises a 404 exception (preferred) |


### 3.6. Summary / Best Practices

* Use **GET** for safe operations (viewing data).
* Use **POST** for operations that modify data.
* Always handle missing parameters gracefully (`get()` with default value or check `None`).
* Prefer `get_object_or_404` instead of manual try/except + `HttpResponseNotFound`.
* Use appropriate HTTP response classes for clarity and standardization.

## 4. HTTP Versions

### 🔹 HTTP/1.1

* Widely used for many years.
* Each request opens a new connection (inefficient for many files like CSS, JS, images).
* Uses **text-based protocol**.

### 🔹 HTTP/2

* Introduces **multiplexing** (multiple requests over one connection).
* Faster loading due to parallelism.
* Binary protocol (more efficient than text).
* Supported by modern browsers and Django when behind a capable web server (e.g., Nginx).

### 🔹 HTTP/3

* Based on **QUIC** (built on UDP instead of TCP).
* Lower latency, faster on unreliable networks.
* Still rolling out, not yet fully adopted everywhere.

