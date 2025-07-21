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

# Module 1: Setting Up


<div class="alert alert-block alert-success">
<b>Module 1 Objectives:</b><br> 
By the end of this module, you will be able to:<br><br>

- Set up Python in various work environments (e.g., terminal, VSCode, Anaconda).<br>

- Understand how to execute Python scripts and work within Jupyter notebooks.<br>

- Test the setup with simple Python code using the print statement.<br>
</div>

## Why Python?

Python is a beginner-friendly programming language with clean, readable synthax that resembles natural human language. It's used for a wide range of tasks, including: 


- Data analysis and manipulation (using libraries like Pandas, NumPy).
- Data visualization (using libraries like Matplotlib, Seaborn, Plotly).
- Statistical analysis and modeling (using libraries like SciPy, Statsmodels, Scikit-learn).
- Building and training machine learning models (using libraries like Scikit-learn, TensorFlow, Keras, PyTorch).


## Python versus R

Python and R are both widely used in data science. We often see debates in the field about whether to use one or the other, as if they were mutually exclusive. 
For beginners, this choice might seem more critical, but in the long term, learning both languages is often necessary. Instead of viewing them as competing options, it's better to consider them as complementary tools, each suited to different tasks or use cases. 

For instance, R is highly specialized in statistical tests and models like mixed-effects models, survival analysis, or time-series forecasting, while Python is ideal for tasks related to deep learning, web development, automation, or deploying models {cite}`datacamp_python_vs_r`.

## Python + Jupyter Notebook = ...?

There are two main files format used for Python codes.

Python scripts (with a .py extension) are plain text files containing Python code. They are used ideally for production code, writing applications and libraries/packages, and reusing functions and classes. However, they have no built-in output visualization and are executed as one whole script.

If you're interested in seeing what your code is doing, you can instead use Jupyter Notebook files (with a .ipynb extension). 
Jupyter notebook files (previously known as Ipython notebook) allow you to create computational notebooks and write your code interatively (not limited to Python). Quoting the [official documentation](https://docs.jupyter.org/en/latest/#what-is-a-notebook), "*A computational notebook is a shareable document that combines computer code, plain language descriptions, data, rich visualizations like 3D models, charts, graphs and figures, and interactive controls*".

In other words,  it's interactive, which allows for step-by-step code execution and for viewing your outputs. It's great for data exploration and analysis since you can easily experiment with Python code and visualize results, as well as add text-based explanations (Markdown).

We'll be using Jupyter Notebook files for exercices, and we'll eventually learn how to use both when required {cite}`jupyter_notebook`.

N.B. Jupyter Notebook refers to both a file format and an application. You can edit .ipynb files in any code editor or IDE!

| **Feature**                | **.py (Python Script)**                                    | **.ipynb (Jupyter Notebook)**                             |
|----------------------------|------------------------------------------------------------|-----------------------------------------------------------|
| **File Format**            | Plain text file containing Python code.                   | JSON file that contains code, text (Markdown), and outputs. |
| **Execution**              | Executed as a whole script.                               | Executed in chunks (cells), output shown after each cell. |
| **Usage**                  | Suitable for production code, apps, and large projects.   | Best for interactive exploration, analysis, and learning.  |
| **Interactivity**          | Linear execution, no interactive output.                  | Interactive execution with immediate feedback and outputs. |
| **Output Visualization**   | No built-in output visualization.                         | Directly supports rich visual outputs like plots and tables. |
| **Documentation**          | Limited to comments in the code.                          | Supports Markdown for rich documentation and formatting.   |



## Where can I write my Python code?

You can write and edit Python code through your terminal. However, you might find it easier and more manageable to use applications like Jupyter Notebook, JupyterLab, VS Code, or even Google Colab.

Code editors or Integrated Development Environments (IDE) let you write Python code in .py or .ipynb format. The key difference between the two is that code editors are primarily used to writing and editing code, while IDEs integrate a suite of programming and software development tools in one interface. However, the line can get blurred as some code editors like VSCode are highly customisable thanks to community plugins. Ultimately, both code editors and IDEs can significantly boost your coding efficiency, simplify your workflow, and make debugging more effective. 
We're using jupyter notebooks to run code so it doesn't matter what editor/environment you end up choosing. 

We'll first talk about how to work with Python in a terminal before moving onto more useful tools like VS Code and Anaconda.


References:
```{bibliography}
```