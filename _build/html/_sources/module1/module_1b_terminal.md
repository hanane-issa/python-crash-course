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

<div class="alert alert-block alert-success">
<b>Section Objectives:</b><br> 
- Understand how Python works in the terminal.<br>
- Upgrade your Python version in the terminal.<br>
</div>


Before we dive into fancy tools like VS Code and Anaconda, let’s start with the basics: running Python from your terminal or command prompt.



## 1. Install Python

If you don’t have Python yet, follow these steps:

Go to the official website: https://www.python.org/downloads {cite}`python_beginners_guide`.

Download the latest stable version (e.g., Python 3.13.2).

On Windows, make sure you check the box that says:

✅ "Add Python to PATH"

Some operating systems, like Linux or macOS, come with a preinstalled version of Python.
If you already have Python installed, skip to step 3.

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

## 4. Using the Python interpreter (REPL)

You can now run Python in interactive mode via your terminal by typing `python` (or `python3`).
You should see something like "Python 3.13.2...."
The `>>>` sign indicates that the interpreter is ready to accept input.


You can run any simple code to test the REPL. Notice how it immediately shows you the output (the lines without `>>>`):

<img src="../_static/images/repl_example.png" alt="python_repl"/>

To quit, simply type:
```bash
exit()
```
```{note}
You can also quit by using ctrl+D.
```


## 5. Upgrading your Python version

Upgrading your Python version differs across operating systems.

### Manually

| **OS**                | **Manual Upgrade Strategy**                                    | **Replaces System Python?**                             |
|-----------------------|----------------------------------------------------------------|---------------------------------------------------------|
| **Windows**           | Download .exe from python.org and install                      | ✅ (if you choose upgrade)                              |
| **macOS**             | Build from source via `curl` + `make`                          | ❌ (safe, manual version install)                       |
| **Linux**             | Build from source via `wget` + `make`                          | ❌ (safe, doesn’t replace system Python)                |



### via Package Manager


| **OS**        | **Tool Example**   |**Upgrade Strategy with Tools**                                    | **Notes**                             |
|-----------------------|------------|--------------------------------------------------------|---------------------------------------------------------|
| **Windows**           | Winget  | `winget upgrade --id Python.Python.3`                     | Preinstalled on Win11                              |
| **macOS**             | Homebrew| `brew upgrade python`                                     |                       |
| **Linux**             |APT      |`sudo apt upgrade python3`                                 |                |



```{note}
You can run Linux commands in Windows using WSL {cite}`wsl`.
```


References:

```{bibliography}
:filter: docname in docnames
```