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




# Installing Python Packages


When you install Python, it comes with a standard library containing pre-installed packages such as:
- os (for interacting with the operating system)

- math (for mathematical operations)

- sys (for system-specific parameters)

- datetime (for date and time manipulation)

However, you still need to import them since Python needs to know which tools you're planning to use.
Think of it as your workshop—you have access to all the tools in the toolbox, but you still have to take the right tool out before you can use it.


```{note}
Why doesn't Python load modules by default?

- It keeps Python fast and lightweight by loading only what's needed.

- It prevents naming conflicts by keeping modules separate until called.

- It lets you explicitly control what your code depends on.
```



## Installing packages with pip

To extend Python's capabilities, you often need to install third-party packages that are not included in the standard library. These packages are installed via pip (from PyPI) and can be anything from data science libraries like numpy and pandas, to web frameworks like Flask or Django, or machine learning tools like scikit-learn.

This process is usually done in your terminal via:
```bash
pip install pandas
```
Where `pandas` is a package for data manipulation and analysis that you'll learn about in module 4.


You can also run this shell command in your jupyter notebook, by adding a ! or % before pip ( [see more on stackoverflow] (https://stackoverflow.com/questions/45784499/what-is-the-difference-between-and-in-jupyter-notebooks) ).

```{code-cell}
!pip install pandas
#same as: %pip install pandas
```
## Installing Specific Versions of Packages

We've mentioned before that, in some cases, you might be working with projects that rely on specific versions of a package. You can specify the package version you want to install:
```{code-cell}
pip install pandas==2.2.3
#replace 2.2.3 with the version you want.
```
A quick way of checking and verifying your package version is via:

```{code-cell}

#import your package
import pandas 

#check your package version
print(pandas.__version__)
```


## Installing Packages from a .tar.gz, .whl, or other file formats

You can also install Python packages directly from remote URLs or local files like .tar.gz and .whl using pip.

```{code-cell}
## from a URL (fake):
#!pip install https://example.com/package.tar.gz

## from a local file:
#!pip install /path/to/package.tar.gz
```

## Creating a requirements file

At some point, you will have a list of packages you often install and import. A nice way to streamline this process, especially if you want to share your work with other programmers, is creating a requirements file.

A requirements.txt file is a simple text file that lists all of the packages your project depends on. It’s common to include the versions of each package you’ve used, ensuring that others who work on the project (or even you, in the future) can install the exact same dependencies.

### Manually

You can do this manually by creating a text file and listing each package name on a new line. You can also specify the package version, for example:

pandas==2.2.3
numpy==2.2.4


### Automatically

If you've already installed the packages in your current environment, you can automatically generate the requirements.txt file with this command:

```{code-cell}
!pip freeze > requirements.txt
```

This command lists all the installed packages and their versions in the current Python environment and saves them in requirements.txt.


```{code-cell}
!pip install -r requirements.txt
```

This will read the requirements.txt file and install the packages listed in it, ensuring that the environment is set up with the correct dependencies.
(Note:this assumes the text file is in the same working directory as your notebook.)

## Importing packages in the next modules

In Python, you can use the *as* keyword to give a module or package an alias, which means you can refer to it by a shorter or more convenient name. This is especially helpful when the package name is long, or when you want to use a commonly accepted alias.

Syntax for Import Aliases
The basic syntax for creating an import alias is:


```{code-cell}
import <module_name> as <alias_name>
```

Where <module_name> is the actual name of the package or module, and  <alias_name> is the shorter or more convenient name you want to use for that package.

```{code-cell}
#Example: 
import pandas as pd
```


```{note}
Why use aliases for imports?
- Convenience: Shorter names make code more readable and less repetitive.
- Consistency: Many libraries (like pandas, numpy, matplotlib, etc.) have common aliases that people use across the community, so it's easier to share and collaborate with others when using these same aliases.
- Readability: Some packages have long names, and using an alias makes the code cleaner and easier to read. That said, there is no need for an alias if the package name is short e.g. os, sys.
- Avoiding name conflicts


```


