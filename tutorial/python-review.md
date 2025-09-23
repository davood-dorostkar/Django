# 📘 Python Review Tutorial

This guide is a structured review of core Python concepts, based on your notes.
All external links and cheat sheets remain exactly as provided.


## 📦 Packages

Django has several **LTS (Long-Term Support)** versions, e.g., `3.2`, `4.2`, `5.2`.
Best practice is to pin your `requirements.txt` to a stable range instead of a fixed version:

```txt
# requirements.txt
Django >=4.2,<4.3
```

### Common `pip` Commands

```sh
pip install package-name
pip install "Django>3,<4"
pip install --upgrade package-name
pip install package.whl
pip uninstall package-name
pip freeze              # show installed packages
pip show package-name   # package details
pip download package-name
```


## 🟣 Tuple

A **tuple** is an ordered, immutable collection. Defined using `()` or just commas.

```py
T1 = (1,)    # single-item tuple (comma required)
T2 = ("Apple", "Banana", "Orange")
T3 = 10, 20, 30, 40, 50   # parentheses optional
```

👉 Parameters passed to a function are internally handled as a tuple.

```py
def example(*args):
    print(args)

example(1, 2, 3)  # (1, 2, 3)
```

### Read more

[link](https://www.w3schools.com/python/python_tuples.asp)


## 🟢 List

Lists are **mutable ordered collections**.

### Slicing

```py
list_variable[start:stop:step]
```

Example:

```py
X = "hello"
print(X[::-1])  # olleh
```

### Copying

```py
list_a = [1, 2, 3]
list_b = list_a[:]   # shallow copy
```

### Read more

* [link](https://www.w3schools.com/python/python_lists.asp)
* [link](https://www.w3schools.com/python/python_strings_slicing.asp)
* [link](https://www.geeksforgeeks.org/python-list-slicing/)


## 🔵 Set

Sets are **unordered collections of unique items**.

Operations:

```py
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print(set1 | set2)   # union
print(set1 & set2)   # intersection
print(set1 - set2)   # difference
print(set1 ^ set2)   # symmetric difference
```

### Read more

* [link](https://www.w3schools.com/python/python_sets.asp)
* [link](https://realpython.com/python-sets/)


## 🟠 Dictionary

Dictionaries store **key-value pairs**.

### Accessing

```py
person = {"name": "Alice", "age": 25}

print(person["name"])        # Alice
print(person.get("email"))   # None (safe)
```

### Updating

```py
person.update({"age": 26, "email": "alice@example.com"})
print(person)
# {'name': 'Alice', 'age': 26, 'email': 'alice@example.com'}
```

### Read more

* [link](https://www.w3schools.com/python/python_dictionaries.asp)
* [link](https://realpython.com/python-dicts/)


## 🔧 Functions

* **Function**: takes objects as parameters.
* **Method**: belongs to a class and works on its objects.

### `*args` and `**kwargs`

* `*args` → collects extra arguments into a tuple.
* `**kwargs` → collects keyword arguments into a dictionary.

```py
def example(*args, **kwargs):
    print("Args:", args)       # tuple
    print("Kwargs:", kwargs)   # dict

example(1, 2, 3, name="Alice", age=25)
```

### Read more

* [link](https://www.w3schools.com/python/python_functions.asp)
* [link](https://www.tutorialspoint.com/python/python_functions.htm)
* [link](https://realpython.com/defining-your-own-python-function/)
* [link](https://www.geeksforgeeks.org/functions-in-python/)


## 🌐 Virtual Environment

Virtual environments isolate dependencies for projects.

```sh
pip install virtualenv
```

Create multiple environments in one project:

```sh
python -m venv venv1
python -m venv venv2
python -m venv venv3
```

Activate & deactivate:

```sh
source my_env/bin/activate   # Linux/macOS
deactivate
```


## ⚠️ Exception Handling

Handle runtime errors gracefully:

```py
try:
    x = 1 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Cleanup runs here")
```

### Read more

[link](https://www.w3schools.com/python/python_try_except.asp)
[link](https://realpython.com/python-exceptions/#:~:text=The%20try%20and%20except%20block%20in%20Python%20is%20used%20to,in%20the%20preceding%20try%20clause.)


## 🏛️ OOP (Object-Oriented Programming)

### Class and Instance

```py
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

a = Human("Davood", 30)
a.email = "aabbcc@gmail.com"  # dynamic attribute
```

* `self` → refers to current instance.
* `super()` → calls parent class method.

### Inheritance Example

```py
class Animal:
    def sound(self):
        print("Some sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Bark")

Dog().sound()
```

### Read more

* [link](https://www.w3schools.com/python/python_inheritance.asp)
* [link](https://www.geeksforgeeks.org/inheritance-in-python/)


## ✨ Magic Methods

Magic (dunder) methods let classes behave like built-ins.

Example:

```py
class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return f"Book: {self.title}"

b = Book("Python 101")
print(b)   # calls __str__
```

### Read more

* [link](https://www.tutorialsteacher.com/python/magic-methods-in-python)
* [link](https://www.geeksforgeeks.org/dunder-magic-methods-python/)
* [link](https://rszalski.github.io/magicmethods/)


## 🌍 Web Scraping

Example with **Selenium + BeautifulSoup**:

```py
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# creating driver object
driver = Chrome(executable_path='chromedriver.exe')

driver.get("https://google.com")
search_bar = driver.find_element_by_name('q')
search_bar.send_keys("آموزش پایتون مکتبخونه")
search_bar.send_keys(Keys.ENTER)

soup = BeautifulSoup(driver.page_source, "html.parser")
name_list = soup.find_all('h3')

with open('names.txt','a',encoding='utf-8') as f:
    for name in name_list:
        f.write(name.text + "\n")
```

Here’s a polished tutorial for **Python’s Walrus Operator (`:=`)** integrated into Django context usage:


## 📝 Python Walrus Operator (`:=`)

The **walrus operator** (`:=`) allows you to **assign a value to a variable as part of an expression**. This can reduce redundancy, especially in `if` statements, loops, or template-related filtering in Django.


### 1. Basic Example

Instead of writing:

```python
value = len(my_list)
if value > 10:
    print(f"List is too long ({value} items)")
```

You can use the **walrus operator**:

```python
if (value := len(my_list)) > 10:
    print(f"List is too long ({value} items)")
```

* `value := len(my_list)` assigns `len(my_list)` to `value` **while checking the condition**.
* Cleaner and avoids computing `len(my_list)` twice.

### 2. Loops with Walrus Operator

```python
while (line := file.readline().strip()) != "":
    print(line)
```

### 3. Key Points

* Only available in **Python 3.8+**
* Useful to **assign variables inside expressions**
* Reduces repetition and makes code cleaner


## 📑 Python Cheat Sheets

* [sheet](/cheat-sheet/PDFtoJPG.me-01.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-04.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-07.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-08.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-09.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-10.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-13.jpg)
* [sheet](/cheat-sheet/PDFtoJPG.me-14.jpg)

