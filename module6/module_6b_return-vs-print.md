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
# Module 6b: Return Statements


<div class="alert alert-block alert-success">
<b>Section Objectives:</b><br> 
- Understand the concept of return values from functions versus functions that only print output without returning values.
</div>

## Functions that print instead of return

Sometimes you may want a function to display something on the screen rather than calculate and return a value. This is common when:

- You're debugging (checking your logic step by step)

- You want to summarize or visualize data directly for the user

- You're building exploratory tools, not reusable computations


Let's modify the smoking count function as an example. We'll add a print statement to help us see what’s going on during execution.

def count_smokers_by_category(df):
    if 'smoking_status' in df.columns:
        print("Column found. Counting smoking categories...")
        return df['smoking_status'].value_counts()
    else:
        print("Column 'smoking_status' not found in DataFrame.")
        return None

`None` represents the absence of value, and has the `NoneType` data type. You'll see other programming languages call it `null`, `nil`, or `undefined`.

Now let’s write a function that doesn't return any value — it just prints a useful summary.

```{code-cell} python
def print_stroke_summary(df):
    total = len(df)
    stroke_count = df['stroke'].sum()
    no_stroke_count = total - stroke_count
    stroke_rate = stroke_count / total * 100

    print("Stroke Summary Report:")
    print(f"Total records: {total}")
    print(f"Stroke cases: {stroke_count}")
    print(f"No stroke cases: {no_stroke_count}")
    print(f"Stroke rate: {stroke_rate:.2f}%")
```

This function prints information to the screen, but doesn't return anything. If you tried to assign its output to a variable, you'd get:


```{code-cell} python
result = print_stroke_summary(df)
print(result)  # Output: None
```
When your function ends with a print statement or doesn't have a return statement, Python adds `return None` behind the scenes. This is also the case when you use the `return` keyword by itself without any value added to the statement.

We've seen a similar behavior with loops; when you write a `for` or `while` loop, Python implicitly adds a `continue` statement.
(source: https://automatetheboringstuff.com/2e/chapter3/ )

## Functions with no return statement

A function does not need a return statement. If it doesn’t return anything explicitly, it still runs — it just returns None by default.

This is common in:

- Plotting and visualization

- Functions designed for side effects (like writing to a file or showing a chart)

In module 5, you learned how to write code to plot a histogram for the average glucose level. Let’s reuse that code, but turn it into a general-purpose display-only function which plots the histogram of any passed column.

```{code-cell} python
def plot_histogram(df, column, bins=30):
    """
    Plot a normalized histogram for any numeric column in the DataFrame.
    
    Parameters:
        df (pd.DataFrame): The dataset.
        column (str): The name of the numeric column to plot.
        bins (int): Number of bins for the histogram (default 30).
    """
    plt.figure(figsize=(6, 4))
    plt.hist(df[column].dropna(), bins=bins, alpha=0.6, edgecolor='black', density=True)
    plt.xlabel(column, fontsize=14)
    plt.ylabel('Probability density', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title(f'Normalized Histogram of {column}', fontsize=18)
    plt.show()
```

Remember that if you want to actually store the figure for later use — like saving it to a file or modifying it, you can update the function to return the figure object as follows: 

```{code-cell} python
def plot_histogram(df, column, bins=30):
    """
    Plot a normalized histogram for any numeric column in the DataFrame.
    
    Parameters:
        df (pd.DataFrame): The dataset.
        column (str): The name of the numeric column to plot.
        bins (int): Number of bins for the histogram (default 30).
    """
    fig = plt.figure(figsize=(6, 4))
    plt.hist(df[column].dropna(), bins=bins, alpha=0.6, edgecolor='black', density=True)
    plt.xlabel(column, fontsize=14)
    plt.ylabel('Probability density', fontsize=14)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.title(f'Normalized Histogram of {column}', fontsize=18)
    plt.show()
    return fig
```

### Functions that return multiple variables

So far, we've seen functions that return one value — like a number or a string. But what if you need to return multiple results from a single function?

In Python, you can do that easily using tuples (see Module _).  When you return multiple values from a function, Python automatically creates a tuple behind the scenes.

🔹 Why would you return multiple values?
Sometimes a function does more than one thing and needs to give back multiple pieces of information. For example:

Suppose you have a dataset of patients. You want a function that counts how many are adults (age 18 or older) and how many are minors (under 18).

```{code-cell} python
def count_adults_and_minors(df):
    """
    Count how many patients are adults (age >= 18) and minors (age < 18).
    
    Parameters:
        df (pd.DataFrame): The stroke dataset with an 'age' column.
    
    Returns:
        tuple: (number_of_adults, number_of_minors)
    """
    adults = df[df["age"] >= 18].shape[0]
    minors = df[df["age"] < 18].shape[0]
    
    return adults, minors
```

```{code-cell} python
adult_count, minor_count = count_adults_and_minors(stroke_data)
```

What the function actually returns is the tuple (adults, minors).
Python automatically unpacks it into two variables: `adult_count` and `minor_count`.

You could assign the tuple to a variable first:

```{code-cell} python
result = count_adults_and_minors(stroke_data)
print(result)
```

Then access the different parts as follows:
```{code-cell} python
print(result[0])  # adults
print(result[1])  # minors
```

But using unpacking (as we did earlier) is cleaner and easier to read.

### Quick Practice

Write a function that does two things:

- Prints the average stroke rate for each smoking status group.

- Plots a bar chart to visualize those averages (check Module 5 or official documentation if you've forgotten how to do this!).

- Optional: returns the plot object so you can store or save it later.


def plot_stroke_by_smoking(df):
    """
    Show average stroke rate by smoking status group.
    
    Parameters:
        df (pd.DataFrame): The stroke dataset.
    
    Returns:
        matplotlib.figure.Figure: The figure object for further use (e.g. saving).
    """
    # Step 1: Group by smoking status and calculate average stroke rate


    # Step 2: Print summary


    # Step 3: Plot


    # Step 4: Return figure

    pass
    


<div style="margin-bottom: 15px;">
  <details>
    <summary>
      <i class="fa fa-lightbulb-o" aria-hidden="true" style="color: yellow; font-size: 20px;"></i> 
      Hint 1
    </summary>
    <p style="padding-left: 20px;">
    To calculate the average of a column grouped by categories in another column, you can use this pattern:<\br>
    grouped_averages = df.groupby('grouping_column')['value_column'].mean() <\br>
    You’ll get a Series where the index contains each unique group from the grouping column, and the values are the calculated averages for each group from the value column.
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
    Use plt.bar() or sns.barplot() to create the chart.
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
def plot_stroke_by_smoking(df):
    """
    Show average stroke rate by smoking status group.
    
    Parameters:
        df (pd.DataFrame): The stroke dataset.
    
    Returns:
        matplotlib.figure.Figure: The figure object for further use (e.g. saving).
    """
    # Step 1: Group by smoking status and calculate average stroke rate
    stroke_rates = df.groupby('smoking_status')['stroke'].mean()

    # Step 2: Print summary
    print("Average stroke rate by smoking status:")
    for group, rate in stroke_rates.items():
        print(f"- {group}: {rate:.3f}")

    # Step 3: Plot
    fig = plt.figure(figsize=(6, 4))
    stroke_rates.plot(kind='bar', color='teal', edgecolor='black')
    plt.title("Stroke Rate by Smoking Status")
    plt.ylabel("Average Stroke Rate")
    plt.xlabel("Smoking Status")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Step 4: Return figure
    return fig
    </code></pre>
  </details>
</div>
