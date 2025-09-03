# Python Review

django 3.2, 4.2, 5.2, ... is LTS. so if you want 4.2 the best practice is to set a range:
```
# requirements.txt

Django >=4.2,<4.3
```
## tuple
in python, `()` shows a tuple. if you want to show a one item tuple you must use `(4,)`. paranthese is optional. ways to define a tuple:
```py
T1 = (1,)    
T2 = ("Apple", "Banana", "Orange")     
T3 = 10,20,30,40,50  
```
### Read more
[link](https://www.w3schools.com/python/python_tuples.asp)

## list

list slicing: `list_varible[start:stop:step]` 

reverse a list: 
```py
X= “hello”
Print(X[::-1]) # olleh
```

copy a list:
```py
list_a = [1,2,3]
list_b = list_a[:]
```
### Read more
- [link](https://www.w3schools.com/python/python_lists.asp)
- [link](https://www.w3schools.com/python/python_strings_slicing.asp)
- [link](https://www.geeksforgeeks.org/python-list-slicing/)

## set
sets operations:
```py
set1 = {1,2,3}
set2 = {3,4,5}

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)
print(set1 ^ set2)
```
### Read more
- [link](https://www.w3schools.com/python/python_sets.asp)
- [link](https://realpython.com/python-sets/)

## dictionary
in dicts you can retrieve with key or with .get . the first gives error, but the latter returns None if it doenst exist.
```py
example
```

can change multiple items with .update
```
example
```
### Read more
- [link](https://www.w3schools.com/python/python_dictionaries.asp)
- [link](https://realpython.com/python-dicts/)


## Python cheat sheets
- [sheet](/cheat-sheet/PDFtoJPG.me-01.jpg)
- [sheet](/cheat-sheet/PDFtoJPG.me-04.jpg)
- [sheet](/cheat-sheet/PDFtoJPG.me-07.jpg)
- [sheet](/cheat-sheet/PDFtoJPG.me-08.jpg)