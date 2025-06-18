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
# Module 6f: Extra (OPTIONAL)


<div class="alert alert-block alert-success">
<b>Section Objectives:</b><br> 
- Learn some useful functions we use often.
</div>

These are some bonus concepts that aren't essential for day-to-day data analysis but are useful to know — and often come up in more advanced tasks and code reading.

## Recursion

A recursive function is a function that calls itself to solve a problem step by step. Recursion is not commonly used for DataFrame operations, but it helps you understand how some algorithms work.

Let’s say we want to calculate a factorial:

```{code-cell} python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
```
`factorial(3)` returns `3 * factorial(2)`, which becomes `3 * 2 * factorial(1)`, and so on…


```{note}
Be careful! Recursive functions must always have a base case (a stopping condition), or they’ll go on forever.
```

## Anonymous (Lambda) Functions

A lambda function is a quick way to define a simple function in one line, without using `def`. It's very useful with `.apply()` in pandas.
Let’s label patients with a bmi_status column, based on their BMI:

```{code-cell} python
stroke_data['bmi_status'] = stroke_data['bmi'].apply(lambda x: 'high' if x > 30 else 'normal')
```

This adds a new column with the label 'high' if BMI is over 30, 'normal' if less or equal to 30.
The code above is the same as writing the following:

```{code-cell} python
def bmi_label(x):
    return 'high' if x > 30 else 'normal'

stroke_data['bmi_status'] = stroke_data['bmi'].apply(bmi_label)
```

## Useful Built-in Functions: `map`, `filter`, and `zip`

These are functions you can use with lists or Series to quickly transform or filter data.

### `map(function, iterable)`

Useful to apply a function to every item in a list or Series.

```{code-cell} python
#Example: Let’s get stroke status labels (string) for each patient.
stroke_flags = stroke_data['stroke'].map(lambda x: 'Yes' if x == 1 else 'No')
```

### `filter(function, iterable)`

Filters a list by a condition that returns True.

```{code-cell} python
#Example: Get a list of patient ages 80 or older
ages = stroke_Data['age'].tolist()
senior_patients = list(filter(lambda x: x >= 80, ages))
```

### `zip(function, iterable)`

Combines two lists into pairs.

```{code-cell} python
#Example: Pair each patient’s ID and age into tuples
patient_ids = stroke_data['id'].head(3)
ages = stroke_data['age'].head(3)

list(zip(patient_ids, ages))
```