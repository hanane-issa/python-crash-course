# M2: Variables

## 3 Variables

### 3.1. Variables

A **variable** is a name that refers to a value. In Python, you do not declare the type – just assign a value and Python figures out the type behind the scenes.

```python
# Assigning values to variables
age = 25
name = "Alice"

print("Age:", age)
print("Name:", name)
```

You can change (reassign) variables at any time.

Variable names must start with a letter or underscore (`_`) and cannot contain spaces or special punctuation (aside from `_`).


### 3.2. Data Types

Before diving into variables, let's see the most common **built-in** data types in Python:

1. **Integer**: Whole numbers, e.g., `42`, `-3`.
2. **Float**: Numbers with a decimal point, e.g., `3.14`, `-0.001`.
3. **String**: Sequences of characters, written inside quotes, e.g., `"Hello, Python!"`.
4. **Boolean**: `True` or `False`.
5. **NonType**: Represented by `None`, means "no value" or "nothing here yet".

```python
# Integers, floats, strings, booleans, and None
my_int = 10
my_float = 3.14
my_str = "Python"
my_bool = True
my_none = None

print(type(my_int))   # <class 'int'>
print(type(my_float)) # <class 'float'>
print(type(my_str))   # <class 'str'>
print(type(my_bool))  # <class 'bool'>
print(type(my_none))  # <class 'NoneType'>
```



### 3.3. Case Sensitivity

Python is **case-sensitive**. For example, `myVariable` and `myvariable` would be treated as different names. Stick to one consistent naming style (*snake_case* is common in Python: `my_variable`).

---

