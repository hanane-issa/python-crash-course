---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


```{image} images/vscode-alt.png
:alt: vscode logo
:class: bg-primary mb-1
:width: 200px
:align: center
```


# Python in VSCode

Virtual Studio Code (VSCode) is a lightweight, open-source code editor  developed by Microsoft for a wide range of programming languages, including Python. It contains a vast library of extensions which allows you to customize your work environment to your needs.

With support for version control (Git), debugging, and code editing, VSC is a comprehensive tool that enables Python developers to write, test, and debug code seamlessly.

Moreover, it has a very active community and plenty of tutorials and documentation available online. 

VSCode works across all major platforms: Windows, macOS, and Linux. 

## 1. Download VSCode

Let's start by downloading the code editor [here](https://code.visualstudio.com/download) and installing it.


## 2. Install Necessary Plugins

You will need to install the Python extension as well as the Jupyter extension.

![vscode_extensions](images/vscode_guide1.png)

## 3. Create a New File

Once you have set up VS Code with the necessary extensions, you can create any file by selecting the following:
File > New File

```{image} images/vscode_newfile.png
:alt: vscode logo
:class: bg-primary mb-1
:width: 500px
:align: center
```

You will be prompted to select a file type, for example a text file, a python file (.py) or a jupyter notebook (.ipynb).

Let's start with a new jupyter notebook file to start writing your first Python code.

## 4. Writing your first Python code

![ipynb gif](images/vscode_firstcode.gif)

As mentioned before, jupyter notebooks allow you to interactively write code (including Python code) and combine it wiht text, images, and graphs.

You can add text and headers to your notebook by selecting Markdown as the programming language for your cell, or selecting "Add Markdown". You can find more information on basic Markdown syntax [here](https://www.markdownguide.org/basic-syntax/).


To begin writing Python code in your notebook, simply change the cell type to Code, or insert a new code cell with Python as the language.

```{code-cell}
# My first code
print("Hello, world!")
```

The print() function is one of the most basic and useful functions in Python. It outputs whatever is inside the parentheses to the screen — in this case, the message "Hello, world!". It's commonly used for displaying messages, debugging, and showing the results of calculations or operations.

In your code cell, adding a dial symbol `#` before a text turns it into a comment. This is a piece of text within the code that is ignored by the computer when the program runs. Comments are used to provide explanations, clarifications, or descriptions about parts of the code, which helps other programmers (or even your future self) understand what the code does.


```{note}
You can press `Shift + Enter` to run your current code cell.
```





