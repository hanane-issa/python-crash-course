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


# Python in Terminal

Before we dive into fancy tools like VS Code and Anaconda, let’s start with the basics: running Python from your terminal or command prompt.



## 1. Install Python

If you don’t have Python yet, follow these steps:

Go to the official website: https://www.python.org/downloads

Download the latest stable version (e.g., Python 3.13.2).

On Windows, make sure you check the box that says:

✅ "Add Python to PATH"

## 2. Open Your Terminal

On Windows: Open the Command Prompt or Anaconda Prompt

On Mac: Open the Terminal app (command key (⌘) + space bar).

On Linux: Open your default terminal (ctrl + alt + T).

## 3. Check your Python version

```bash
python --version
```

```{note}
Depending on your operating system and how Python is installed, this might not work. 
In this case, use "python3" instead of "python".
```

## 4. Using the Python interpreter

You can now run Python in interactive mode via your terminal by typing `python` (or `python3`).
You should see something like "Python 3.13.2....
Type "help", "copyright", "credits" or "license" for more information."

To quit, simply type:
```bash
exit()
```