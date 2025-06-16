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
# Module 6: Local vs Global Variables


<div class="alert alert-block alert-success">
<b>Section Objectives:</b><br> 
- Differentiate between local and global variables
</div>

When working with functions, it’s important to understand where your variables "live" — in other words, their scope.

A local variable exists only inside the function where it was defined.

A global variable exists outside all functions and can be used throughout your code.

Understanding the difference will help you avoid unexpected behavior when naming variables or modifying data.

## Local Variables

Local variables are created and used inside a function. They disappear once the function finishes running.

```{code-cell} python
def count_stroke_cases(df):
    stroke_count = df['stroke'].sum()  
    print("Number of stroke cases:", stroke_count)
```
The `stroke_count` variable is created locally inside the function. If you try to use it outside the function, Python will raise an error:  

```{code-cell} python
count_stroke_cases(stroke_data)
print(stroke_count)  # ❌ NameError: name 'stroke_count' is not defined
```

## Global Variables

A global variable is defined outside any function and can be accessed inside functions (but not modified unless explicitly declared as global).


stroke_column = 'stroke'  # global variable

```{code-cell} python
def count_stroke_cases(df):
    print("Stroke count:", df[stroke_column].sum())
```
This works because stroke_column is defined in the global scope, and we’re only reading it.

## ⚠️ Modifying Global Variables Inside Functions

If you try to change a global variable inside a function, Python treats it as a new local variable unless you tell it otherwise with the global keyword.


count = 0  # global variable

```{code-cell} python
def update_count():
    count = count + 1  # ❌ UnboundLocalError
```


To modify a global variable safely, you must declare it:


count = 0
```{code-cell} python
def update_count():
    global count
    count += 1
```

But in most cases, it’s better to **avoid** modifying global variables inside functions. Instead, return a value from the function and update the variable outside:


count = 0

```{code-cell} python
def count_high_glucose(df, threshold):
    return (df['avg_glucose_level'] > threshold).sum()

count = count_high_glucose(stroke_data, 125)
```

```{note}
Use local variables as much as possible. They keep your functions self-contained, predictable, and easier to debug.
```

## Quick Practice

What will happen in this code?

```{code-cell} python
threshold = 130  # global

def check_threshold(df):
    threshold = 110  # local
    print("Local threshold:", threshold)
    print("Patients above threshold:", (df['avg_glucose_level'] > threshold).sum())

check_threshold(stroke_data)
print("Global threshold is still:", threshold)
```

<div style="margin-bottom: 15px;">
  <details>
    <summary>
      <i class="fa fa-lightbulb" aria-hidden="true" style="color: yellow; font-size: 20px;"></i> 
      Answer
    </summary>
    <p style="padding-left: 20px;">
    <pre><code class="python">
The global `threshold` remains 130. Inside the function, `threshold` is a new local variable set to 110 and doesn’t affect the global one.
  </details>
</div>