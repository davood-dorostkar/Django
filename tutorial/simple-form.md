# 📝 Django Forms

## Why Use Django Forms?

When building web apps, handling user input is critical. If you rely on **naive methods** (directly saving `request.POST` data), you risk invalid or malicious input.

Django provides a **Forms framework** that:

* Validates input automatically.
* Cleans and normalizes data.
* Protects against security issues.
* Helps render forms easily in templates.


## 1. Defining Forms

Each app should have a `forms.py` file where forms are defined.

Example:

```python
# forms.py
from django import forms

class NameForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(required=True)
    age = forms.IntegerField(min_value=1, max_value=120)
```

* `forms.Form` is the base class for custom forms.
* Fields (`CharField`, `EmailField`, `IntegerField`, etc.) automatically handle type validation and constraints.

✅ This ensures invalid data (like text in the age field) won’t even reach your model.


## 2. Handling Forms in Views

The **workflow** is:

* For **GET requests**, display an empty form.
* For **POST requests**, validate and process the submitted form.

```python
# views.py
from django.shortcuts import render, redirect
from .forms import NameForm

def get_name(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            # cleaned_data gives safe, validated values
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            
            # You could save to DB here
            print(f"Received: {name}, {email}, {age}")
            
            return redirect("success")
    else:
        form = NameForm()  # empty form for GET request

    return render(request, "name_form.html", {"form": form})
```

### What is `cleaned_data`?

* After validation (`form.is_valid()`), Django stores **cleaned, safe values** in `form.cleaned_data`.
* It converts input to proper Python types:

  * `"25"` → `25` (int)
  * `"  user@example.com "` → `"user@example.com"` (stripped and validated)
* You should always use `cleaned_data`, not raw `request.POST`.


## 3. Rendering Forms in Templates

Django forms can be rendered **automatically** or with **manual control**.

### Automatic rendering

```django
<form method="post">
  {% csrf_token %}
  {{ form }}
  <button type="submit">Submit</button>
</form>
```

### With formatting helpers

```django
{{ form.as_p }}   <!-- renders each field wrapped in <p> -->
{{ form.as_ul }}  <!-- renders each field in <li> -->
{{ form.as_table }} <!-- renders in <tr><td> style -->
```

### Manual rendering (full control)

```django
<form method="post">
  {% csrf_token %}
  {{ form.name.label_tag }} {{ form.name }}
  {{ form.email.label_tag }} {{ form.email }}
  {{ form.age.label_tag }} {{ form.age }}
  <button type="submit">Submit</button>
</form>
```


## 4. Using Forms with Models

Instead of manually creating model instances with form data, Django recommends using **ModelForms**.

Example:

```python
# forms.py
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]
```

View:

```python
def add_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # automatically creates and saves a Post instance
            return redirect("post_list")
    else:
        form = PostForm()

    return render(request, "add_post.html", {"form": form})
```

✅ This is the **recommended approach** for working with database models, since it combines validation + object creation in one step.


## 5. Django Forms Workflow

Here’s how data flows when using Django forms:

![Django form workflow](/tutorial/img/form-flow.png)

1. User submits HTML form.
2. Django creates `Form` instance with submitted data.
3. Call `form.is_valid()` → runs validators.
4. If valid → data available in `cleaned_data`.
5. Save data manually or via `form.save()` (if using `ModelForm`).
6. Redirect or re-render with errors if invalid.


## 📚 Read More

* [Django Forms Documentation](https://docs.djangoproject.com/en/3.2/topics/forms/)
* [Django Book – Forms](https://djangobook.com/mdj2-django-forms/)


✅ **Summary**:

* Use Django Forms instead of naive handling for **safety and convenience**.
* `cleaned_data` ensures all inputs are valid and properly typed.
* Templates can auto-render forms or give you full control.
* Use **ModelForms** when working with models to reduce boilerplate.
