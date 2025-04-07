# Module 2 : Foundations

## 2.1. What is Python?


---

## 2.2. Python Syntax Basics


### 2.2.1. Indentation and Code Blocks

In Python, **indentation** is not just for making the code look neat – it defines the **code blocks**. Other languages might use curly braces { } or keywords to group statements, but Python uses **whitespace** (spaces or tabs) at the start of lines.

Below is an example of an `if` statement with indentation. The line `print("You are an adult.")` is indented to indicate it belongs to the `if` statement’s code block.

```python
# Example of a simple if statement with indentation
age = 20
if age >= 18:
    print("You are an adult.")
```

Do not worry if you are not familiar with the specific details in the code above yet, we will learn them throughout this course! The most important takeaway here is that **consistent indentation is crucial**. If the indentation in your code is inconsistent, Python will raise an *error*!


### 2.2.2. Comments

**Comments** are lines or parts of lines that Python does not execute. They can be use to explain your code or to temporarily disable it.

We find two types of comments: **single-line comments** and **multi-line comments**.

- **Single-line comments:** Start with `#`, for example:
```python
# This is a single-line comment.
print("Hello, World!")  # This part is also a comment.
```

- **Multi-line comments:** Use triple quotes `"""` or `'''`, for example:
```python
"""
This is a multi-line comment.
It can span multiple lines.
"""
```


### 2.2.3. Case Sensitivity

Python is **case-sensitive**. For example, `myVariable` and `myvariable` would be treated as different names. Stick to one consistent naming style (*snake_case* is common in Python: `my_variable`).


### 2.2.4. Basic Print Statements

The `print()` function is handy for displaying output on the screen. You can quickly test if your code is doing what you expect by printing results at various stages.

```python
print("Hello, Python!")
```


---


## 2.3. Data Types

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


### 2.3.1. Variables

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


---

## 2.4. Operators and Expressions

**Expressions** are pieces of code that produce a value. They often involve **operators** – symbols or keywords that tell Python what kind of operation to perform.

### 2.4.1. Arithmetic Operators

| **Operator** |   **Description**   | **Example** | **Result** |
| :----------: | :-----------------: | :---------: | :--------: |
|      +       |      Addition       |    3 + 2    |     5      |
|      -       |     Subtraction     |    3 - 2    |     1      |
|      *       |   Multiplication    |    3 * 2    |     6      |
|      /       |  Division (float)   |    3 / 2    |    1.5     |
|      //      |   Floor Division    |   3 // 2    |     1      |
|      %       | Modulus (remainder) |    3 % 2    |     1      |
|      **      |   Exponentiation    |   3 ** 2    |     9      |

```python
a = 10
b = 3

sum_result = a + b # Output: 13
division_result = a / b # Output: 3.3333...
mod_result = a % b # Output: 1

print("Sum:", sum_result)
print("Division:", division_result)
print("Remainder:", mod_result)
```

### 2.4.2. Comparison Operators

Used to compute two values; the result is always a **Boolean** (`True` or `False`).

| **Operator** | **Description**  | **Example** | **Result** |
| :----------: | :--------------: | :---------: | :--------: |
|      ==      |     Equal to     |   3 == 2    |   False    |
|      !=      |   Not equal to   |   3 != 2    |    True    |
|      >       |   Greater than   |    3 > 2    |    True    |
|      <       |    Less than     |    3 < 2    |   False    |
|      >=      | Greater or equal |   3 >= 3    |    True    |
|      <=      |  Less or equal   |   3 <= 2    |   False    |

### 2.4.3. Logical Operators

Operate on **Boolean** values (`True` or `False`) and return also a **Boolean**.

| **Operator** |                **Description**                 |     **Example**     | **Result** |
| :----------: | :--------------------------------------------: | :-----------------: | :--------: |
|     and      |      True if **both** conditions are True      | (3 > 2) and (2 > 1) |    True    |
|      or      |   True if **at least one** condition is True   | (3 > 2) or (2 == 1) |    True    |
|     not      | Inverts the Boolean value (True becomes False) |     not (3 > 2)     |   False    |

```python
print((3 > 2) and (4 > 5)) # Output: False
print((2 < 5) or (10 < 3)) # Output: True
print(not (1 == 1)) # Output: False
```

### 2.4.4. Combining Operators into Expressions

You can combine multiple operators in a single expression. Python follows standard **order of operations** (sometimes called PEMDAS in math):
1. Parentheses.
2. Exponents
3. Multiplication / Division.
4. Addition / Subtraction.

```python
result = 3 + 5 * 2 # Multiplication done first => 3 + 10 = 13.
print(result)

parenthesized_result = (3 + 5) * 2 # Parentheses first => 8 * 2 = 16.
print(parenthesized_result)
```


---
