# Django Messages Framework

The **messages framework** in Django provides a way to temporarily store messages (such as success, error, or info) for a single request–response cycle.

It’s often used to give **feedback to users** after actions like submitting a form, logging in, or updating data.

## Example Usage

**views.py**

```py
from django.contrib import messages
from django.shortcuts import redirect

def submit_form(request):
    # some logic...
    messages.success(request, "Your form was submitted successfully!")
    messages.error(request, "Something went wrong.")
    return redirect("home")
```

**template.html**

```django
{% if messages %}
  <ul>
    {% for message in messages %}
      <li>{{ message }}</li>
    {% endfor %}
  </ul>
{% endif %}
```

Django automatically attaches message levels such as:

* `messages.debug`
* `messages.info`
* `messages.success`
* `messages.warning`
* `messages.error`

## How It Works

1. View logic adds a message.
2. Django attaches it to the request.
3. On the next page load, the template can display it.
4. After rendering, the message disappears.

## Read More

* 📖 [Django Docs – Messages](https://docs.djangoproject.com/en/3.2/ref/contrib/messages/)
* 📖 [Ordinary Coders Guide](https://ordinarycoders.com/blog/article/django-messages-framework)
* 📖 [Display Messages After Form Submit](https://www.csestack.org/display-messages-form-submit-django/)
