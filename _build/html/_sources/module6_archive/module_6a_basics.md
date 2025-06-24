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
# Module 6a: Function Basics

<div class="alert alert-block alert-success">
<b>Module 1 Objectives:</b><br> 
By the end of this module, you will be able to:<br><br>

- Understand how to define a function in a programming language.<br> 
- Learn how to call a function to execute its code.<br>
- Understand the concept of return values from functions versus functions that only print output without returning values.<br>
- Differentiate between local and global variables.<br>
- Write and utilize docstrings to document functions.<br> 
- Differentiate between arguments and parameters in functions.<br>
- Recognize how the number of arguments affects function calls and definitions.<br> 
- Implement default parameter values in function definitions.<br> 
</div>

In the previous sections, we've talked about several built-in functions like `print()` and `input()`, as well as functions from installed packages like numpy's `array()` and pandas' `read_csv()`.

Now we'll talk about how you can write your own functions.


<div class="alert alert-block alert-success">
<b>Section Objectives:</b><br> 
- Understand how to define a function in a programming language.<br> 
- Learn how to call a function to execute its code.<br>
</div>



## Why write a function? 

1. Reuse code easily
As you start coding and analyzing data in Python, you'll soon realize that some code snippets are repeated and can be reused. Instead of copying and pasting the same code again and again, you write it once as a function and use it whenever you need. This saves time and effort!

2. Make your code cleaner and shorter
Functions help break big problems into smaller, manageable pieces. This makes your code easier to read and understand. We often talk about avoiding 'spaghetti code'. Just as it sounds, this describes code that is unclear, a big tangled mess that’s tough to read, understand, and work with,—kind of like a bowl of spaghetti all mixed up. 

3. Avoid mistakes
When you reuse the same function, you only need to test and fix the code once. This reduces errors compared to copying code multiple times.

4. Organize your work
Functions let you give a name to a block of code, which describes what it does. This helps others (and future you!) understand your program faster.

## Anatomy of a Function

So what are the building blocks of a function? What elements do we need for Python to understand that we're defining a function?

Let's take a look at the syntax needed:

<img src="../_static/images/function_annotation.png" alt="function_explanation" style="width: 1400px; height: 300px"/>

As you can see, a function requires parameters to define the type and number of values that it can accept (source: {cite} @params_vs_args). These parameters are placeholders for the actual data you want to pass when you call the function. If your function were a vending machine, then the parameters are the buttons you press to choose what comes out!


```{note}
You only need to define a function once, then you can use (call) it as many times as you like.
```

Let's use the Kaggle stroke data {cite}`kaggle_stroke_prediction` to write our first function.
The stroke variable is binary: 1 indicates that the patient had a stroke, and 0 indicates the absence of a stroke. We can then determine the number of patients who had a stroke by calculating the sum of this column through the following function:

```{code-cell} python
def count_stroke_patients(df):
    """
    Return the number of patients in the dataset who had a stroke.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataset containing patient information. Must include a 'stroke' column
        with binary values (e.g., 0 = no stroke, 1 = stroke).

    Returns
    -------
    int
        The number of patients who had a stroke.
    """
    stroke_count = df['stroke'].sum()
    return stroke_count
```

To call the function, we use the syntax `function_name(arguments)`.

```{code-cell} python
:tags: [remove-output]
count_stroke_patients(stroke_data)
```

## The Pass Statement:  A Placeholder for Code

Sometimes, when writing functions, classes, or loops, you know what you want to build — but not how just yet. You can use a `pass` statement as a placeholder to build your code and test it without any issue.

### What does `pass` do? 

The pass statement tells Python:

“Do nothing here, but don’t crash.”

It’s useful when you're outlining code and want to avoid errors while the logic is still incomplete.

Suppose you're planning to write a function that will analyze the relationship between smoking status and stroke, but you're not ready to write the actual logic yet.

```{code-cell} python
def analyze_smoking_effect(df):
    pass  # We'll implement this later
```
You can call this function, and Python won’t complain — it just won’t do anything yet.

### `pass` in Conditionals

You might also check if the smoking_status column exists, but want to fill in the logic later:

```{code-cell} python
if 'smoking_status' in df.columns:
    pass  # analysis will go here
else:
    print("Column 'smoking_status' not found.")
```

This code runs without error, even though the if block is empty for now.


### What happens if we remove `pass`?

```{code-cell} python
def analyze_smoking_effect(df):
    # nothing here!
```
If you remove the `pass` statement, you'll be faced with an `IndentationError`, because Python expects at least one statement in a function.


### Mini-Exercice 

Complete the function below to:

- Check if the 'smoking_status' column exists

- If yes, return a pandas Series with counts of each smoking category using .value_counts()

- If no, return a message saying the column isn’t found.

The pass statement is a placeholder you can replace with real code when you’re ready.
You can call the function to see if it works!


def count_smokers_by_category(df):
    if 'smoking_status' in df.columns:
        pass
        ### TO DO: REPLACE PASS WITH YOUR CODE ###
    else:
        pass
        ### TO DO: REPLACE PASS WITH YOUR CODE ###





<div style="margin-bottom: 15px;">
  <details>
    <summary>
      <i class="fa fa-lightbulb" aria-hidden="true" style="color: yellow; font-size: 20px;"></i> 
      Solution
    </summary>
    <p style="padding-left: 20px;">
    </p>
    <pre><code class="python">
def count_smokers_by_category(df):
    if 'smoking_status' in df.columns:
        return df['smoking_status'].value_counts()
    else:
        return "Column 'smoking_status' not found."
    </code></pre>
  </details>
</div>
