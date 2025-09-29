# 📝 Rich Text Editors in Django

By default, **Django escapes HTML tags** inside templates to prevent security risks like XSS.
If you want to render HTML safely, you can use the `safe` filter:

```django
{{ content|safe }}
```


## 1. Popular Rich Text Editors

* [TinyMCE](https://github.com/jazzband/django-tinymce)
* [CKEditor](https://github.com/django-ckeditor/django-ckeditor)
* [Summernote](https://github.com/lqez/django-summernote) ✅ (we’ll use this one as example)


## 2. Setup Summernote

### Installation

```bash
pip install django-summernote
```

### Settings

```python
INSTALLED_APPS = [
    ...
    "django_summernote",
]
```

### URLs

```python
from django.urls import path, include

urlpatterns = [
    ...
    path("summernote/", include("django_summernote.urls")),
]
```

### Media Config (required for uploads)

```python
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media/")
```

Run migrations:

```bash
python manage.py migrate
```

👉 This creates new tables for managing uploaded files.


## 3. Using Summernote in Django Admin

You can integrate Summernote with the Django Admin easily:

```python
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)  # Apply Summernote to 'content' field

admin.site.register(Post, PostAdmin)
```


## 4. Using Summernote in Forms

Apply Summernote as a widget in forms:

```python
from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import SomeModel

# Standard Summernote widget (iframe mode)
class SomeForm(forms.Form):
    foo = forms.CharField(widget=SummernoteWidget())

# Inplace widget (no iframe, works with Bootstrap/jQuery themes)
class AnotherForm(forms.Form):
    bar = forms.CharField(widget=SummernoteInplaceWidget())

# ModelForm with Summernote widgets
class FormFromSomeModel(forms.ModelForm):
    class Meta:
        model = SomeModel
        fields = "__all__"
        widgets = {
            "foo": SummernoteWidget(),
            "bar": SummernoteInplaceWidget(),
        }
```


## 5. Customization with `SUMMERNOTE_CONFIG`

You can configure Summernote in `settings.py`:

```python
SUMMERNOTE_CONFIG = {
    "iframe": True,   # Use iframe mode (default). Set False for inplace mode.

    "summernote": {
        "width": "100%",
        "height": "480",
        "toolbar": [
            ["style", ["style"]],
            ["font", ["bold", "underline", "clear"]],
            ["insert", ["link", "picture", "video"]],
            ["view", ["fullscreen", "codeview", "help"]],
        ],
    },

    # Require authentication for uploads
    "attachment_require_authentication": True,

    # Customize where uploads are stored
    # "attachment_upload_to": my_custom_upload_to_func,

    # Completely disable file uploads if needed
    "disable_attachment": False,
}
```


## 6. How It Works

* Uploaded files are stored in your **`MEDIA_ROOT`**.
* The database only keeps a reference (path + metadata).
* Summernote renders HTML content directly in your templates (`{{ post.content|safe }}`).


## 7. Fixing Same-Origin iFrame Issues

If you face **iFrame Same-Origin Policy** problems:

* Switch to **inplace widget mode** (`iframe: False`), or
* Set `X_FRAME_OPTIONS = 'SAMEORIGIN'` into `settings.py`


## 8. Read More

* [Django Summernote Docs](https://github.com/lqez/django-summernote)
* [Summernote Editor Features](https://summernote.org/)

