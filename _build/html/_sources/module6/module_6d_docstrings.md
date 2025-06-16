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
```{code-cell} python
:tags: [remove-input]

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
stroke_data = pd.read_csv("../data/healthcare-dataset-stroke-data.csv")
```
# Module 6: Docstrings

<div class="alert alert-block alert-success">
<b>Section Objectives:</b><br> 
- Write and utilize docstrings to document functions.<br> 
</div>



## Docstrings

Let's go back to the `ount_stroke_patients()` function. Notice how we had a multi-line string in triple quotes, also called documentation string or **docstring** for short. The docstring links explanatory documentation to Python objects such as functions, modules, and classes. It explains the purpose of the function, as well as the parameters required,and the output/return we get. 
It is incredibly useful for others (as well as future you!) to develop this good practice. 

You can access an object's documentation through the `__doc__` method or `help()` function.


```{code-cell} python
print("Using __doc__:")
print(count_stroke_patients.__doc__)

print("Using help:")
help(count_stroke_patients)
```

For the sake of standardization, there a few conventions to follow when writing a docstring, mainly based on {cite} @pep_257  and common community practices (see: {cite} @python_docstrings):


1) Basic Syntax Rules
- Use """triple double quotes""" even for one-liners.

- Place the docstring immediately after the def or class line.

- For raw strings (e.g., with backslashes), use r"""insert raw docstring here""".
- Stick to one format, for example the Numpydoc Style used in the `count_stroke_patients()` function.

2) One-line Docstrings
- Used for simple functions or when a brief summary suffices.

- Format:

    - Triple quotes on a single line.

    - No blank line after.

    - Imperative mood: "Return..." not "Returns..."

    - End with a period.

    Example:
    ```{code-cell} python
    :tags: [remove-output]
    def func_example1(df):
    """Return the number of patients with stroke."""
    ```

3) Multi-line Docstrings

- Format:

    - First line: summary, fits on one line.

    - Blank line after summary.

    - Optional: detailed description (behavior, arguments, exceptions, return).

    - Closing """ on its own line if the docstring spans multiple lines.

    Example: see example function in building blocks section.

