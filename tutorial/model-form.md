# 📝 Django ModelForms

## Why ModelForms?

While regular Django **Forms** let you define fields manually, **ModelForms** automatically generate forms from existing models.

This provides:

* Automatic mapping between **form fields** and **model fields**.
* Built-in validation based on model constraints.
* Simplified saving with `form.save()`.

✅ With ModelForms, you don’t need to manually handle saving form data into models — Django does it for you.


## 1. Defining a ModelForm

Let’s say we have a simple `Contact` model:

```python
# models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

Now, create a `forms.py`:

```python
# forms.py
from django.forms import ModelForm
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"  # include all fields from the model
```


## 2. Controlling Fields

You can decide which fields appear in the form:

* **Include all fields**

  ```python
  fields = "__all__"
  ```

* **Include only specific fields**

  ```python
  fields = ["name", "email"]
  ```

* **Exclude specific fields**

  ```python
  exclude = ["created_at"]
  ```


## 3. Customizing Widgets

Widgets control how a field is rendered in HTML (e.g., `TextInput`, `Textarea`, `EmailInput`).

```python
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter your name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter your email"}),
            "message": forms.Textarea(attrs={"rows": 5, "class": "form-control"}),
        }
```

✅ This makes your form more user-friendly and integrates well with CSS frameworks like **Bootstrap**.


## 4. Using ModelForms in Views

The workflow is very similar to normal forms:

```python
# views.py
from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()  # directly saves to DB!
            return redirect("success")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})
```


## 5. Rendering in Templates

```django
<!-- contact.html -->
<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Send</button>
</form>
```

Or manually render each field if you want more control:

```django
<p>{{ form.name.label_tag }} {{ form.name }}</p>
<p>{{ form.email.label_tag }} {{ form.email }}</p>
<p>{{ form.message.label_tag }} {{ form.message }}</p>
```


## 6. Why ModelForms Are Recommended

* Less boilerplate: You don’t have to write form fields manually.
* Automatic validation: Uses model constraints like `max_length`, `unique`, etc.
* Easy saving: Just call `form.save()`.
* Customizable: You can still add widgets, validators, or custom methods.


## 📚 Read More

* [GeeksforGeeks – Django Forms](https://www.geeksforgeeks.org/django-forms/)
* [MDN – Django Forms](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms)


✅ **Summary**:
ModelForms let you quickly create forms tied to database models. They reduce boilerplate, provide automatic validation, and make saving data as simple as calling `form.save()`. You can still customize which fields appear and how they’re rendered using `fields`, `exclude`, and `widgets`.
