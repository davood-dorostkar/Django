# Database Fields

## image field
you need to install pillow package

use ImageField

### options
- upload_to
by default it uploads to media folder. if you define a folder, it will be relative to media.
example

- upload to speicific dir based on date

- the image is actually saved into media folder and it only keeps its address in the db.

⚠️ if you delete a media file from db, it wont be removed from disk as well.

- default (uses default media if not provided)

- using post.image.url in templates
- if used file with existing name, django automaticlaly changes the name (postfixes a random text)

### read more
- [link](https://docs.djangoproject.com/en/3.2/topics/files/)
- [link](https://www.geeksforgeeks.org/imagefield-django-models/)
- [link](https://djangocentral.com/uploading-images-with-django/)

## category field
```
class category:
    name = 

class post:
    category = manytomany
```
```django
{% for cat in post.category.all %}
{{cat.name}}
{% endfor %}
```
or 
```
{{ post.category.all|join:", " }}
```
- when using a many to many field, an third table is created that stores only the relations between two tables.


### read more
- [link](https://docs.djangoproject.com/en/3.2/topics/db/examples/many_to_many/)

- [link](https://www.revsys.com/tidbits/tips-using-djangos-manytomanyfield/)