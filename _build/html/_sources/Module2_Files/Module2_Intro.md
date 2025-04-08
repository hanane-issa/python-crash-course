# M2: Introduction 

## 1 What is Python?

*Blah blah blah...*

---

## 2 Python Syntax Basics


### 2.1. Indentation and Code Blocks

In Python, **indentation** is not just for making the code look neat – it defines the **code blocks**. Other languages might use curly braces { } or keywords to group statements, but Python uses **whitespace** (spaces or tabs) at the start of lines.

Below is an example of an `if` statement with indentation. The line `print("You are an adult.")` is indented to indicate it belongs to the `if` statement’s code block.

```python
# Example of a simple if statement with indentation
age = 20
if age >= 18:
    print("You are an adult.")
```

Do not worry if you are not familiar with the specific details in the code above yet, we will learn them throughout this course! The most important takeaway here is that **consistent indentation is crucial**. If the indentation in your code is inconsistent, Python will raise an *error*!


### 2.2. Comments

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

### 2.3. Basic Print Statements

The `print()` function is handy for displaying output on the screen. You can quickly test if your code is doing what you expect by printing results at various stages.

```python
print("Hello, Python!")
```


---

