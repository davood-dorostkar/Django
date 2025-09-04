# Django Introduction

use `wappalyzer` chrome extension to check the technologies used in a website.

## optional: create a venv
```sh
python -m pip install --upgrade pip
python -m venv venv
. venv/bin/activate
```

## Install and start a project
```sh
python -m pip install --upgrade pip
pip install "django>4.2,<4.3"
# or
pip install -r requirements.txt
```

to create a project without creating extra nested folders use current directory:
```sh
django-admin startproject mysite .
```
if you dont mention `.`, it will create  the project in `mysite/mysite`

run it:
```sh
python manage.py migrate
python manage.py runserver
```

## 📑 Django Cheat Sheets

* [sheet](/cheat-sheet/PDFtoJPG.me-23.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-24.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-25.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-26.jpg)
