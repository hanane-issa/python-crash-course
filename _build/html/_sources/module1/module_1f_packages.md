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

<div class="alert alert-block alert-success">
<b>Section Objectives:</b><br> 
- Install and import Python packages.<br> 
- Keep track of package versions.<br> 
</div>

Python has a wide range of packages (pre-installed or third-party) that offer extra features like functions, data, and code to your programs.
When you install Python, it comes with a standard library containing pre-installed packages such as:
- os (for interacting with the operating system)

- math (for mathematical operations)

- sys (for system-specific parameters)

- datetime (for date and time manipulation)

However, you still need to import them since Python needs to know which tools you're planning to use.
Think of it as your workshop—you have access to all the tools in the toolbox, but you still have to take the right tool out before you can use it.
You can find a list of built-in Python modules [here](https://docs.python.org/3/py-modindex.html).

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
:tags: [skip-execution]

!pip install pandas
#same as: %pip install pandas
```
## Installing Specific Versions of Packages

We've mentioned before that, in some cases, you might be working with projects that rely on specific versions of a package. You can specify the package version you want to install:
```{code-cell}
:tags: [skip-execution]

!pip install pandas==2.2.3
#replace 2.2.3 with the version you want.
```
A quick way of checking and verifying your package version is via:

```{code-cell}
:tags: [skip-execution]

#import your package
import pandas 

#check your package version
print(pandas.__version__)
```


## Installing Packages from a .tar.gz, .whl, or other file formats

You can also install Python packages directly from remote URLs or local files like .tar.gz and .whl using pip.

```{code-cell}
:tags: [skip-execution]

## from a URL (fake):
#!pip install https://example.com/package.tar.gz

## from a local file:
#!pip install /path/to/package.tar.gz
```

## `pip` vs `conda` for Package Installation


We've seen in the Anaconda section that `conda` can also be used to install and manage packages.
So what's the difference between `pip` and `conda`?

Although they are very similar, these tools are built for different purposes.

The first key difference to remember is that Pip installs Python packages only, whereas conda can install packages which can contain software written in any language.

Conda also has built-in support for creating isolated environments that can contain different versions of Python and packages, while Pip doesn't and has to depend on other tools like `virtualenv` or `venv`.

You can read more about the differences between conda and pip in this [Anaconda article](https://www.anaconda.com/blog/understanding-conda-and-pip).

## Creating a requirements file (pip)

At some point, you will have a list of packages you often install and import. A nice way to streamline this process, especially if you want to share your work with other programmers, is creating a requirements file.

A requirements.txt file is a simple text file that lists all of the packages your project depends on. It’s common to include the versions of each package you’ve used, ensuring that others who work on the project (or even you, in the future) can install the exact same dependencies.

### Manually

You can do this manually by creating a text file and listing each package name on a new line. You can also specify the package version, for example:

pandas==2.2.3
numpy==2.2.4


### Automatically

If you've already installed the packages in your current environment, you can automatically generate the requirements.txt file with this command:

```{code-cell}
:tags: [skip-execution]
!pip freeze > requirements.txt
```

This command lists all the installed packages and their versions in the current Python environment and saves them in requirements.txt.


```{code-cell}
:tags: [skip-execution]
!pip install -r requirements.txt
```

This will read the requirements.txt file and install the packages listed in it, ensuring that the environment is set up with the correct dependencies.
(Note:this assumes the text file is in the same working directory as your notebook.)

## Creating an environment file (conda)

If you are using conda, you can create a `environment.yml` file.

### Manually

A simple environment YAML file has the `.yml` extension and follows this format:

```yaml
name: myenv
dependencies:
  - numpy
  - pandas
```

You can read more about it [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually).

### Automatically

In your terminal, you can create the `environment.yml` file using the following steps:

1) Create your file:
```bash
conda env create -f environment.yml
```

2) Activate your new environment:
```bash
conda activate myenv
```

3) Verify that your installation was successful:
```bash
conda env list
```

4) Update your enrivonment:
If one of your core dependencies updates, you need an additional package, or you want to replace a package, you can update the contents of your `environment.yml` file accordingly then run this command:

```bash
conda env update --file environment.yml  --prune
```

```{note}
The `--prune` option tells conda to remove any dependencies you no longer require in your environment.
```

You can learn more about commands to manage your conda environments [here] (https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

# Importing Python Packages

## Importing packages in the next modules

In Python, you can use the *as* keyword to give a module or package an alias, which means you can refer to it by a shorter or more convenient name. This is especially helpful when the package name is long, or when you want to use a commonly accepted alias.

Syntax for Import Aliases
The basic syntax for creating an import alias is:


```{code-cell}
:tags: [skip-execution]
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

## Importing specific items from packages

Now you have your workbench ready, and you know how to get your toolbox!
To make things more tidy and easier to work with, it might be more useful to specify what tools you need.

Think of it like in a biology lab. When you’re preparing equipment for a DNA extraction, you don’t bring out the entire lab cabinet. You just take the pipette, buffer, and centrifuge—the tools you need.
In the same way, in Python, importing only what you need keeps your workspace clean and avoids confusion.

### Importing a single item

The syntax we're looking for is `from <module_name> import <item_name>`.
We'll use the `statistics` built-in module as an example.

Let's say you want to calculate the Body Mass Index (BMI) of a patient. You'll need the `pow()` function the `math` module to raise the height value to the power of 2.

```{code-cell}

from math import pow  

weight_kg = 70
height_m = 1.75

bmi = weight_kg / pow(height_m, 2)

```
You can also use an alias for the imported item, e.g.:  `from math import pow as power`.

### Importing several items at once

Some modules are especially useful for your analysis, and while you may not need the entire module, you might still want to import several specific functions from it.

To take the previous example a step further, you want to make sure your BMI value is rounded up to the nearest whole integer using the  `ceil` function. 

```{code-cell}
from math import pow, ceil  

weight_kg = 70
height_m = 1.75

bmi = weight_kg / pow(height_m, 2)
bmi_ceil = ceil(bmi)

```

```{note}
While not recommended, another way to import a whole package is through the syntax:
`from <module_name> import * `
```

### Importing custom packages

You can create your own packages. In the previous sections, we saw how easy it is to create a Python script file called `first_script.py`. If this file contained functions or variables, you can reuse them by importing the file just like a Python module.

```python
import first_script
```

Just like any module, you can also give it an alias.

```python
import first_script as fs
```