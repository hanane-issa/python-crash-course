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
# Module 6e: Parameters and Arguments

<div class="alert alert-block alert-success">
<b>Section Objectives:</b><br> 
- Differentiate between arguments and parameters in functions.<br>
- Recognize how the number of arguments affects function calls and definitions.<br> 
- Implement default parameter values in function definitions.
</div>



## Parameters vs Arguments

In programming, we differentiate between the variable names declared in the function, and the actual variables passed in the function.

A **parameter** is the placeholder variable name you declare in the function. It is part of the function's signature.
An **argument** is the actual variable or value you pass in the function when you call it.

Let's go back to the `count_stroke_patients()` function to understand the difference better.


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

When we defined this function, we used **df** as the parameter. It isn't a real dataset; it is an indicator for you to know that the function requires a dataframe that will be used in its code.
(Source: {cite} @params_vs_args)

```{code-cell} python
:tags: [remove-output]
count_stroke_patients(stroke_data)
```
When we called this function, we used the dataframe **stroke_data** as the argument. This is the actual data we want the function to work with.

```{note}
It's good practice to use meaningful parameter names. It makes your code more understandable and easier to maintain.
```


## Multiple Parameters, Multiple Arguments

Functions can have more than one parameter. This allows you to pass multiple pieces of information into it. 
When you call the function, you must provide the same number of arguments (unless some parameters have default values, which you'll learn later).

The order matters — the first argument goes to the first parameter, the second to the second, etc.

This is called **positional arguments** (we’ll discuss keyword arguments later).

```{code-cell} python
def patient_summary(df, column):
    """
    Print the average value for a given column in the dataframe.
    """
    avg_value = df[column].mean()
    print(f"The average {column} is {avg_value:.2f}")
```
With two parameters, we call the function with two arguments as follows:

```{code-cell} python
patient_summary(stroke_data, "age")
patient_summary(stroke_data, "avg_glucose_level")
```


Try switching the argument order to see what the function does:

```{code-cell} python
### Your code here ###
```
## Default parameters/default arguments

You can give your function parameters a default value so that callers don’t have to provide every argument every time. These are called default parameters or optional arguments.

```{code-cell} python
def check_high_glucose(df, threshold=125):
    """
    Add a column 'glucose_status' labeling patients as 'high' or 'normal'
    based on avg_glucose_level threshold.
    """
    def glucose_level(glucose):
        if glucose > threshold:
            return 'high'
        else:
            return 'normal'
    
    df['glucose_status'] = df['avg_glucose_level'].apply(glucose_level)
    return df
```
The parameter threshold has a default value of 125.

If you call the function without specifying threshold, it will use 125.


```{code-cell} python
check_high_glucose(stroke_data)  # Uses default threshold = 125
```
But you can override it by passing your own value:

```{code-cell} python
check_high_glucose(stroke_data, threshold=140)  
```

```{note}
- Use default values only when it makes sense. For example, if there’s a common or typical value that fits most cases, it’s helpful to set it as a default. 
- Parameters with default values must come after parameters without defaults.
- You cannot have a required parameter after a default one.
```

## Positional vs Keyword arguments

### Using positional arguments
You might have noticed by now that,even without default arguments, the order of called arguments matters.
Arguments are matched to parameters based on their position — first with first, second with second, and so on.
You must pass them in the same sequence the function expects.
Let's take a look at the following function:

```{code-cell} python
def describe_patient(df, index, age_col, gender_col, hypertension_col):
    """
    Print a basic description of a patient at the given index.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataset containing patient information.
    index : int
        The row index of the patient in the dataset.
    age_col : str
        Name of the column containing age information.
    gender_col : str
        Name of the column containing gender information.
    hypertension_col : str
        Name of the column indicating whether the patient has hypertension (0 or 1).

    Returns
    -------
    None
        This function only prints output to the screen.
    """
    patient = df.iloc[index]
    
    print(f"Patient #{index}: {patient[age_col]}-year-old {patient[gender_col]}.")
    
    if patient[hypertension_col]:
        print("Has hypertension.")
    else:
        print("No hypertension.")
```

To call the function and follow the correct positional argument order, we use:

```{code-cell} python
describe_patient(stroke_data, 10, 'age', 'gender', 'hypertension')
```
`stroke_data` goes to `df`, `10` goes to 10 goes to `index`, `age` goes to `age_col`, `gender` goes to `gender_col`, and `hypertension` goes to `hypertension_col`.

What happens if we swap the arguments `'age'` and `'gender'`?

```{code-cell} python
describe_patient(stroke_data, 10, 'gender', 'age', 'hypertension')
```
You’ll get nonsense output because Python assigns 'Male' to index (which should be an int), and so on.

### Using keyword arguments
You can explicitly specify which argument refers back to which parameter in your function as follows:

```{code-cell} python
describe_patient(
    df=stroke_data,
    index=10,
    age_col='age',
    gender_col='gender',
    hypertension_col='hypertension'
)
```
The order then no longer matters since Python assigns the values based on the parameter names.

## Arbitrary positional arguments (`*args`)

Sometimes, you don’t know in advance how many positional arguments someone will pass.

The *args syntax collects all extra positional arguments into a **tuple**.

Let's try a different function which shows you patient data based on the index provided:

```{code-cell} python
def show_patient_columns(df, index, *columns):
    """
    Print specified column values for a patient at a given index.
    
    Parameters:
        df (pd.DataFrame): The dataset.
        index (int): Patient row index.
        *columns (str): One or more column names to display.
    """
    patient = df.iloc[index]
    print(f"Patient #{index} data:")
    for col in columns:
        print(f"{col}: {patient[col]}")
```
Since we are using arbitrary positional arguments or *args, you can call the function with any number of columns:

```{code-cell} python
show_patient_columns(stroke_data, 10, 'age', 'bmi', 'avg_glucose_level')
```
## Arbitrary keywords arguments (`**kwargs`)

The `**kwargs` syntax collects any extra keyword arguments into a **dictionary**, allowing flexible labeled data input.
Arguments are passed as key=value pairs, and the function accesses them by key name.

```{code-cell} python
def patient_summary(df, index, **info):
    """
    Print a summary report for a specific patient, including extra labeled information.

    Parameters
    ----------
    df : pandas.DataFrame
        The stroke dataset containing patient data.
    index : int
        The row index of the patient in the DataFrame.
    **info : dict
        Arbitrary keyword arguments where keys are labels and values are either
        column names in `df` or literal information to print.

    Returns
    -------
    None
        Prints the summary information without returning any value.
    """
    patient = df.iloc[index]
    print(f"Summary for patient #{index}:")
    for label, col_name in info.items():
        if col_name in df.columns:
            print(f"{label.capitalize()}: {patient[col_name]}")
        else:
            print(f"{label.capitalize()}: {col_name}")  # literal if not a column
```
We call it like this:

```{code-cell} python
patient_summary(
    stroke_data,
    7,
    age='age',
    gender='gender',
    smoker='smoking_status'
)
```

Here, info is a dictionary: {'age': 'age', 'gender': 'gender', 'smoker': 'smoking_status'}.

## `*args` vs `**kwargs`

Both `*args` and `**kwargs` let your functions accept an arbitrary number of arguments beyond those explicitly declared, but they work differently:

| Aspect             | `*args`                            | `**kwargs`                     |
| ------------------ | ---------------------------------- | ------------------------------ |
| Collects           | Extra positional arguments (tuple) | Extra keyword arguments (dict) |
| Usage              | When number/order of args vary     | When number/names of args vary |
| How to pass        | Without keywords, just values      | Using `key=value` pairs        |
| Access in function | By position (iteration over tuple) | By keys (iteration over dict)  |
| Example use case   | Columns list to print              | Named patient info or options  |
| Flexibility        | Flexible number but no labels      | Flexible number and labels     |


TLDR;
- Use `*args` if you want to accept many values without caring about their names, like a list of columns.

- Use `**kwargs` if you want to accept many options or labeled data, where each argument’s name matters.

## Quick Practice
`*args` and `**kwargs` not mutually exclusive. You can combine both in a function!

Write a function named patient_report that:

1) Takes these parameters:

    - df: the stroke dataset DataFrame

    - index: an integer representing the patient row index

    - *columns: any number of column names to display

    - **extra_info: any number of keyword arguments with extra info to print

2) Prints a report for the patient at the given index:

    - For each column in *columns, print the column name and that patient's value.

    - For each key-value pair in **extra_info, print the key (capitalized) and the value as is.






<div style="margin-bottom: 15px;">
  <details>
    <summary>
      <i class="fa fa-lightbulb-o" aria-hidden="true" style="color: yellow; font-size: 20px;"></i> 
      Hint 1
    </summary>
    <p style="padding-left: 20px;">
    Use .capitalize() on the keys from extra_info for nicer formatting.
    </p>
  </details>
</div>

<div style="margin-bottom: 15px;">
  <details>
    <summary>
      <i class="fa fa-lightbulb-o" aria-hidden="true" style="color: yellow; font-size: 20px;"></i> 
      Hint 2
    </summary>
    <p style="padding-left: 20px;">
    Loop over columns (the *args) to print each requested column and value.
    Loop over extra_info.items() (the **kwargs) to print each key-value pair.
    </p>
  </details>
</div>

<div style="margin-bottom: 15px;">
  <details>
    <summary>
      <i class="fa fa-lightbulb" aria-hidden="true" style="color: yellow; font-size: 20px;"></i> 
      Solution
    </summary>
    <p style="padding-left: 20px;">
    <pre><code class="python">
```{code-cell} python
def patient_report(df, index, *columns, **extra_info):
    """
    Print a detailed report for a specific patient in the DataFrame.

    Parameters
    ----------
    df : pandas.DataFrame
        The stroke dataset containing patient data.
    index : int
        The row index of the patient in the DataFrame.
    *columns : str
        Variable length argument list of column names to display values for.
    **extra_info : dict
        Arbitrary keyword arguments representing additional labeled information to include in the report.
    
    Returns
    -------
    None
        This function prints the patient report directly and does not return a value.
    """
    patient = df.iloc[index]
    print(f"Patient #{index} report:")
    for col in columns:
        print(f"{col}: {patient[col]}")
    for key, val in extra_info.items():
        print(f"{key.capitalize()}: {val}")
```
    </code></pre>
  </details>
</div>





