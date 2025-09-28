# 🎨 Enhance Forms UI with Django Crispy (Optional)

By default, Django forms render as plain HTML, which may look unpolished. **Crispy Forms** is a Django app that helps you:

* Render beautiful forms with minimal effort.
* Integrate directly with CSS frameworks (Bootstrap, Tailwind, etc.).
* Add layouts, placeholders, columns, and buttons in a structured way.


## 1. Installation

Install crispy forms and a CSS framework pack (Bootstrap is most common):

```bash
pip install django-crispy-forms crispy-bootstrap5
```


## 2. Configuration

Add crispy apps to your `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "crispy_forms",
    "crispy_bootstrap5",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
```


## 3. Using Crispy in Templates

In your template:

```django
{% load crispy_forms_tags %}

<form method="post">
  {% csrf_token %}
  {{ form|crispy }}
  <button type="submit" class="btn btn-primary">Submit</button>
</form>
```

✅ This will automatically apply Bootstrap styling.


## 4. FormHelper and Layouts

For more customization, define a **FormHelper** in your form class:

```python
# forms.py
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Row, Column
from crispy_forms.bootstrap import InlineRadios
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = "post"
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-2"
        self.helper.field_class = "col-md-8"

        self.helper.layout = Layout(
            Row(
                Column(Field("name", placeholder="Enter your full name"), css_class="col-md-6"),
                Column(Field("email", placeholder="Enter your email"), css_class="col-md-6"),
            ),
            Field("message", rows="5", placeholder="Type your message"),
            InlineRadios("category"),  # example radio field
            Submit("submit", "Send Message", css_class="btn btn-success"),
        )
```

### Features:

* **`Field`** → allows adding placeholders, `rows`, `cols`, and CSS classes.
* **`Row` and `Column`** → create grid-based layouts.
* **`InlineRadios`** → display radio buttons inline.
* **`Submit`** → adds styled submit buttons.


## 5. Adding Validation

You can define custom validators inside your form:

```python
def clean_name(self):
    name = self.cleaned_data.get("name")
    if len(name) < 3:
        raise forms.ValidationError("Name must be at least 3 characters long.")
    return name
```

This integrates seamlessly with Crispy, and errors will be displayed with Bootstrap styling.


## ✅ Summary

* **Crispy Forms** makes Django forms look professional with minimal effort.
* Supports multiple frameworks (Bootstrap 4/5, Tailwind, etc.).
* Provides **FormHelper**, **Layouts**, and **Field customization** for maximum flexibility.
* Adds **validation** support with clean integration into styled forms.


## 📚 Read More

* [Crispy Forms Documentation](https://django-crispy-forms.readthedocs.io/en/latest/)
