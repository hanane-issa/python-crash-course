# M2: Introduction 

## 1 What is Python?

Python is one of the most common programming languages currently in various fields including Bioinformatics. This is due to its simple, easy to learn syntax which mimics natural languages, which makes it easy to write, learn, and read. Python is a general purpose programming language suitable for many different tasks. There exists a large collection of open-source Python packages/libraries to support its usage for any purpose. Through this course you will get to know some of these which are very handy for Bioinformatics, e.g. `numpy` and `pandas`.

Python is a object-oriented programming (OOP) language. This means that the code is organised around data, i.e. objects, instead of functions or logic. This helps to maintain and keep an overview over complex code. If you not familiar with OOP and this explanation does not make fully sense yet, don't worry about it. We will get back to it in chapter ... .

For now we will concentrate on getting familiar with basic Python syntax and elements, before carrying on to more complex aspects in the later chapters. Through all of this we will be using examples from Bioinformatics to help you learn the language in the context of our interests. 

## 2 Python Syntax Basics
The first thing needed to understand is how Python code is organised and structured, i.e. its syntax.

### 2.1. Indentation and Code Blocks
Python assumes that each new statement start on a new line. This eliminates the need of a semicolon `;` at the end of the statement, as is the standard in many other programming language.

Similarly, **code blocks** are defined in Python by using **indentation**. Other languages might use curly braces `{ }` or keywords to group statements, but Python uses **whitespace** (spaces or tabs) at the start of lines. One ident corresponds with one tab (<kbd>tab</kbd>) or four spaces (<kbd>space</kbd>). When indenting you create a child of the previous line. Often the parents have a colon `:` at the end (see chapter [](M2-conditional-blocks-header) for statement examples which use colons). One can have multiple indentation/blocks nested within each other. To end a block, simply outdent (<kbd>tab</kbd> + <kbd>Shift</kbd>). At the end of a parent block it is common to leave a line of whitespace before starting the next block.

```python
im_a_parent:
    im_a_child:
        im_a_grandchild
        im_a_second_grandchild
    im_a_second_child:
        im_a_third__grand_child

im_a_new_parent:
    im_a_new_child
```

These syntax rules do not only keep your code need but makes it easier and quicker to write it and eliminates easy to make mistakes (e.g. forgetting to put a semicolon at the end).

Below is an example of an `if` statement with indentation. The `if` statement checks whether the `age` variable is over 18. The line `print("You are an adult.")` is indented to indicate it belongs to/ is a child of the `if` statement’s code block. It is only carried out if `age` is over 18. Do not worry if you are not familiar with the specific details in the code snipped yet, we will learn them throughout this course! The most important takeaway here is that **consistent indentation is crucial**. If the indentation in your code is inconsistent, Python will raise an *error*!

```python
age = 20

if age >= 18:
    print("You are an adult.")
```

### 2.2. Comments

**Comments** are lines or parts of lines that Python does not execute. They can be use to explain your code. It is very useful to have them through out ones code. When other people read your code (or even when you read it in the future) it is often hard to understand what it is trying to achieve based on the executable lines alone. Having comments alongside them, explaining their purpose, makes understanding the code a lot easier.

Comments are also useful when debugging code since they can be used to temporarily disable lines. Just remember to either uncomment or delete the disabled line later to keep your code need!

There are two types of comments: **single-line comments** and **multi-line comments**.

- **Single-line comments:** Start the comment text with a hashtag `#`, for example:
```python
# This is a single-line comment.
print("Hello, World!")  # This part is also a comment.
```

- **Multi-line comments:** Use triple quotes (`"""` or `'''`) around the comment text, for example:
```python
"""
This is a multi-line comment.
It can span multiple lines.
"""
```

### 2.3. Basic Print Statements
While not technically syntax, the `print()` function is a very useful statement, which is why we introduce it now. It is used for displaying output on the screen. You can quickly test if your code is doing what you expect by printing results at various stages.

```python
print("Hello, Python!")
```
