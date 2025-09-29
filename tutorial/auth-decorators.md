# 🛡️ Django Auth Decorators

Django provides **authentication decorators** to restrict access to views based on user authentication or permissions. They are a simple yet powerful way to protect views without writing repetitive checks.

---

## 🔹 What Are They?

* **Decorators** wrap views with extra functionality.
* **Auth decorators** ensure only authenticated or authorized users can access certain views.
* If a condition fails (e.g., user not logged in), the decorator redirects or returns an error response.

---

## 🔹 Function-Based Views vs Class-Based Views

* **Function-Based Views (FBV)** → apply decorators directly:

  ```python
  @login_required
  def dashboard(request):
      ...
  ```

* **Class-Based Views (CBV)** → use `@method_decorator` on `dispatch` (or individual methods):

  ```python
  from django.utils.decorators import method_decorator
  from django.contrib.auth.decorators import login_required
  from django.views import View

  @method_decorator(login_required, name="dispatch")
  class DashboardView(View):
      def get(self, request):
          ...
  ```

---

## 1. `login_required`

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

---

## 2. Other Important Decorators

| Decorator                                | Purpose                                                                                               | Example                                               |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `@login_required`                        | Require user to be authenticated.                                                                     | `@login_required def view(request): ...`              |
| `@permission_required("app.permission")` | Require specific permission. Redirects to login if not logged in, raises `403` if permission missing. | `@permission_required("blog.add_post")`               |
| `@user_passes_test(test_func)`           | Require custom condition (returns `True`/`False`).                                                    | `@user_passes_test(lambda u: u.is_superuser)`         |
| `@staff_member_required`                 | Require `is_staff=True`. Commonly used for admin-only views.                                          | `@staff_member_required def admin_view(request): ...` |

---

## ✅ Key Notes

* `login_required` does **not** check `is_active`. Inactive users are rejected by auth backends.
* You can customize the login page with `settings.LOGIN_URL` or `login_url` argument.
* For **admin-like restrictions**, use `staff_member_required`.
* For **granular control**, use `permission_required` or `user_passes_test`.
