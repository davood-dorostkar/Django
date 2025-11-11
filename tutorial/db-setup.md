# Setting Up a Database Schema with dbdiagram.io


## 1. Introduction to dbdiagram.io

**dbdiagram.io** is a free, web-based ER (Entity-Relationship) diagramming tool. You can:

* Write schema definitions in a simple SQL-like syntax.
* Automatically visualize relationships between tables.
* Export the design to SQL or image formats.
* Share and collaborate with others easily.


## 2. Creating a New Diagram

1. Visit [dbdiagram.io](https://dbdiagram.io).
2. Log in with your GitHub, Google, or email account.
3. Click **“New Diagram”**.
4. On the editor page, write your schema definition in the text editor on the left.
5. The right panel will display the automatically generated ER diagram.


## 3. Syntax Overview

The dbdiagram syntax resembles SQL but is simplified for readability.

### Basic Structure

```sql
table TableName {
  column_name data_type [constraints]
}
```

Common data types include:

* `int`
* `varchar`
* `text`
* `boolean`
* `datetime`
* `char`
* `file` (for references like images or uploads)

### Common Constraints

| Constraint                  | Description                        |
| --------------------------- | ---------------------------------- |
| `pk`                        | Primary Key                        |
| `increment`                 | Auto-increment integer             |
| `unique`                    | Must be unique                     |
| `not null`                  | Cannot be null                     |
| `ref: > other_table.column` | Defines a foreign key relationship |


## 4. Example: Django Blog Database Design

Here’s a sample schema for a Django-based blog application with users, posts, categories, and profiles.

```sql
table User {
  id int [pk, increment] 
  email varchar
  is_staff boolean
  is_active boolean
  type char
  created_date datetime
  updated_date datetime
}

table Profile {
  id int [pk, increment] 
  user int
  first_name varchar
  last_name varchar
  image file
  bio text
}

table Category {
  id int [pk, increment]
  name varchar
}

table Post {
  id int [pk, increment] 
  author int 
  title varchar
  content text
  category int
  published boolean
  published_date datetime
  created_date datetime
  updated_date datetime
}

Ref: "User"."id" < "Profile"."user"
Ref: "Profile"."id" < "Post"."author"
Ref: "Category"."id" < "Post"."category"
```


## 5. Understanding the Relationships

| Relationship      | Description                                  |
| ----------------- | -------------------------------------------- |
| `User → Profile`  | Each user has one profile.                   |
| `Profile → Post`  | Each post is authored by a profile (person). |
| `Category → Post` | Each post belongs to one category.           |

These relationships visually appear as arrows in dbdiagram.io, clearly showing one-to-many (1:N) connections.


## 6. Using the GUI to Create Relationships

While text-based definitions are powerful, dbdiagram also provides a **drag-and-drop GUI** to:

* Create tables manually.
* Add fields and set data types.
* Draw relationships between columns visually.

This can be especially helpful for non-developers or for quickly sketching relationships before refining the schema text.


## 7. Exporting and Using the Diagram

After completing your design:

1. Click the **Export** button on the top right.
2. You can export as:

   * **SQL script** (for MySQL, PostgreSQL, or SQLite)
   * **Image (PNG or SVG)** for documentation
   * **dbml file** (dbdiagram’s native format)
3. Use the exported SQL file to create your database schema directly in Django migrations or initialize your database manually.

Example command to apply SQL schema in PostgreSQL:

```bash
psql -U username -d database_name -f schema.sql
```


## 8. Example Output

The resulting ER diagram should look like this:

![Database Schema Example](/tutorial/img/db-setup.png)


## 9. Tips and Best Practices

* Always define **primary keys** explicitly (`id int [pk, increment]`).
* Keep **naming conventions consistent** (e.g., lowercase with underscores).
* Define **foreign key relationships** explicitly using `Ref` syntax.
* Use **datetime** fields for tracking creation and update times.
* When working with Django:

  * Each table typically maps to a **Django model**.
  * Relationships like `Ref` correspond to Django’s `ForeignKey` or `OneToOneField`.

Example Django model equivalent:

```python
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profiles/')
    bio = models.TextField()
```
