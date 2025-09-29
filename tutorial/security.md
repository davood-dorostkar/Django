# 🔒 Django Security

Keeping your Django project secure is critical before deploying it to production. Django provides many built-in security features, but you should also use external tools to harden your app.


## ✅ Use Mozilla Observatory

* Test your site with **[Mozilla Observatory](https://observatory.mozilla.org/)**.
* It analyzes your web app’s security headers and practices.
* Each failed/bad item can usually be fixed by searching **“<issue> + django”**.


## 🛡️ Django Security Guidelines

Django has a great official guide: [Django Security Documentation](https://docs.djangoproject.com/en/3.2/topics/security/).
It covers:

* 🔑 **Secret key management**
* 🧩 **Cross-Site Scripting (XSS) protection**
* 🚫 **Cross-Site Request Forgery (CSRF) protection**
* 🔐 **SQL injection prevention**
* ✅ **Clickjacking protection**
* 🔒 **HTTPS and secure cookies**


## 📘 Read More

* [10 Tips for Making Django Admin More Secure](https://opensource.com/article/18/1/10-tips-making-django-admin-more-secure)
* [Django Security Tips (Snyk)](https://snyk.io/blog/django-security-tips/)
* [Django Security Checklist (Dev.to)](https://dev.to/coderasha/django-web-security-checklist-before-deployment-secure-your-django-app-4jb8)
