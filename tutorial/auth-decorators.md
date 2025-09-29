# 🛡️ Django Auth Decorators

Django provides **authentication decorators** to restrict access to views based on user authentication or permissions. They are a simple yet powerful way to protect views without writing repetitive checks.

They can be used with:

* **Function-based views (FBVs)** — most common usage.
* **Class-based views (CBVs)** — used via `method_decorator` on specific methods.

## Usage (Function-based views)

apply decorators directly:

```python
@login_required
def dashboard(request):
    ...
```
* Optional custom login URL:

```python
@login_required(login_url='/accounts/login/')
def dashboard(request):
    ...
```
## Usage (Class-based views)

use `@method_decorator` on `dispatch` (or individual methods):

  ```python
  from django.utils.decorators import method_decorator
  from django.contrib.auth.decorators import login_required
  from django.views import View

  @method_decorator(login_required, name="dispatch")
  class DashboardView(View):
      def get(self, request):
          ...
  ```


## `login_required`

The most common decorator.

### How It Works

* If the user **is not logged in** → redirect to `settings.LOGIN_URL` (default: `/accounts/login/`) and append `?next=/requested/path/`.
* If the user **is logged in** → allow access.

### Example (FBV)

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    return HttpResponse("Welcome!")
```

### Example with Custom Login URL

```python
@login_required(login_url="/custom-login/")
def special_view(request):
    ...
```

### Example (CBV)

```python
@method_decorator(login_required, name="dispatch")
class ProfileView(View):
    def get(self, request):
        return HttpResponse("Profile Page")
```


### Notes:

* `login_required` **does not check** the `is_active` flag on users.

  * The default `AUTHENTICATION_BACKENDS` automatically prevent inactive users from logging in.
* For admin-like views, you can use `staff_member_required()` instead.
* 
## Other Important Auth Decorators

| Decorator                                | Purpose                                                                                               | Example                                               |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `@login_required`                        | Require user to be authenticated.                                                                     | `@login_required def view(request): ...`              |
| `@permission_required("app.permission")` | Require specific permission. Redirects to login if not logged in, raises `403` if permission missing. | `@permission_required("blog.add_post")`               |
| `@user_passes_test(test_func)`           | Require custom condition (returns `True`/`False`).                                                    | `@user_passes_test(lambda u: u.is_superuser)`         |
| `@staff_member_required`                 | Require `is_staff=True`. Commonly used for admin-only views.                                          | `@staff_member_required def admin_view(request): ...` |
| `login_required` + `@permission_required`              | Combine decorators          | Can chain multiple decorators on a view    

### Example with permission:

```python
from django.contrib.auth.decorators import permission_required

@permission_required('blog.change_post', raise_exception=True)
def edit_post(request, post_id):
    ...
```

### Example with custom test:

```python
from django.contrib.auth.decorators import user_passes_test

def is_superuser(user):
    return user.is_superuser

@user_passes_test(is_superuser)
def super_dashboard(request):
    ...
```

## Read More

* [Django Authentication Decorators](https://docs.djangoproject.com/en/3.2/topics/auth/default/#the-login-required-decorator)
* [Django Permissions and Authorization](https://docs.djangoproject.com/en/3.2/topics/auth/default/#permissions)