# Welcome to Module 5

In this module, we will go through how to visualize data using Python. We will use 2 very popular packages to do so: Matplotlib and Seaborn.

If you have not done so already, install both Matplotlib and Seaborn by running the following command in the terminal:

```
pip install matplotlib seaborn scikit-learn numpy pandas
```

We will be using the [Stroke Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?resource=download) from Kaggle.

This module assumes that you have gone through module 4 and learned how to load data and handle a dataframe in Python.


# Data visualization with Matpotlib and Seaborn

To get started, in your Jupyter notebook or your Python environment, import the necessary packages:

```
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
```

## Import the dataset

First, let's import the dataset. Make sure the file is in your Python working directory or specify the path to the file.

```
path_to_file = '/the/path/to/healthcare-dataset-stroke-data.csv'
stroke_data = pd.read_csv(path_to_file)
```

## A little bit of data preprocessing

If you check the dataframe with the following code, you will see there are missing values in the bmi.

```
stroke_data.isnull().sum()
```

You should have learned how to handle missing values in module 4. For simplicity, we will replace the missing values with the mean.

```
### getting the bmi mean for non-null values
bmi_mean = stroke_data[~stroke_data['bmi'].isna()]['bmi'].mean()
### filling the missing bmi values with the mean
na_index = stroke_data[stroke_data['bmi'].isna()].index
stroke_data.loc[na_index, 'bmi'] = bmi_mean
```

If we check again, there should be no missing values now.

```
stroke_data.isnull().sum()
```

## Matplotlib and histogram

Let's start simple and try to plot a histogram. For example, if you want to check the distribution of a column e.g. avg_glucose_level, you can do so using a histogram with the following codes:

```
plt.hist(stroke_data.avg_glucose_level, bins=30, alpha=0.6, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Probability density')
plt.title('Normalized Histogram (Density)')
plt.show()
```
We used the function `plt.hist()` from the Matplotlib package to make the plot. As the first argument, we input the data from the dataframe `stroke_data.avg_glucose_level`. The argument `bins` will control how many bins you want - the higher the number the more bins there are. `alpha` allows you to change the transparency of the bins. `black` will add outlines to the bins.

`plt.xlabel()` and `plt.ylabel()` will set the labels of your x-axis and y-axis respectively. `plt.title()` will set the title of the plot. Finally `plt.show()` will actually display the plot.

If you want to know more about the `matplotlib.pyplot.hist()` function and its arguments, go the the [matplotlib documentation](https://matplotlib.org/stable/).


### Changing font size and plot size

While we have the fairly simple example of the histogram, let's try and change the fonts of the plot.

What we will change:
1. size of the plot
2. font size of the x-axis and y-axis label
3. font size of ticks on the x and y-axis

Here are the codes:
```
plt.figure(figsize=(6, 4))
plt.hist(stroke_data.avg_glucose_level, bins=30, alpha=0.6, edgecolor='black')
plt.xlabel('Value', fontsize=14)
plt.ylabel('Probability density',fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.title('Normalized Histogram (Density)', fontsize=18)
plt.show()
```

As you can see, it is quite straightforward. We just have to add the argument `fontsize` in some functions, the number indicate how big you want the font to be (the higher, the bigger). 
The `plt.figure()` function was added at the beginning to control the size of the plot. The two numbers 6 and 4 tell Python that I want the plot to be 6 inches wide and 4 inches high.

### Saving the plot

Now that you have a beautiful figure, you might want to save it. You can do so by using this function `plt.savefig()`. Several formats are supported, most commonly PDF, PNG and JPEG. 

You can save the figure by typing:
```
plt.savefig('avg_glucose_level_histogram.pdf', dpi=300, bbox_inches='tight')
```

`avg_glucose_level_histogram.pdf` is the file name you want to save as, the extension `.pdf` tells Python what format you want to save as. Use `.png` if you want PNG or `.jpg` if you want JPEG. 

`dpi` controls the resolution - the higher the number, the higher the resolution. `bbox_inches='tight'` tells Python to figure out the tightest bounding box of the plot and try to fit it into the specified figure size.

If you just want to save the figure, replace `plt.show()` with `plt.savefig()`. If you want to save AND display the figure, make sure to put `plt.savefig()` before `plt.show()`. 

## Seaborn and scatter plot

We will now try to make a scatter plot. We will also use a new package [Seaborn](https://seaborn.pydata.org/). According to the documentation, `seaborn` 'builds on top of matplotlib and integrates closely with `pandas` data structures'.

Let us plot a scatter plot of BMI vs age by using the following code:

```
plt.figure(figsize=(6, 4))
sns.scatterplot(data=stroke_data, x='age', y='bmi')
plt.title('Scatter plot of BMI vs age')
plt.show()
```

We used the function `sns.scatterplot()` from the `seaborn` package. Here we can put the entire dataframe as the input, then we specify the columns on in the dataframe that we want as x-axis and y-axis like so: `x='age', y='bmi'`

An advantage of using `seaborn` is that, we do not have to explicitly set axis labels, it is automatically done. You can still cutomize the labels by adding the following lines before `plt.show()`:

```
plt.xlabel('AGE', fontsize=14)
plt.ylabel('BMI',fontsize=14)
```


### Color

If you want to display another information on the scatter plot, you can try by adding color to it. We can do this by adding an argument to the function like so:

```
sns.scatterplot(data=stroke_data, x='age', y='bmi', hue='stroke', alpha=0.6)
```
By adding `hue='stroke`, we are telling `seaborn` to color the dots in the scatter plot according to the information in the 'stroke' column.

However, if you try the line of code above you will find that the dots are overlapping and we cannot visualize the color well.

We can try specifying the order of which the dots are plotted for better visualization. The codes are:

```
plt.figure(figsize=(6, 4))
sns.scatterplot(data=stroke_data[stroke_data['stroke']==0], x='age', y='bmi', alpha=0.6)
sns.scatterplot(data=stroke_data[stroke_data['stroke']==1], x='age', y='bmi', alpha=0.6)
plt.title('Scatter plot of BMI vs age')
plt.show()
```


### Multiple plots

Now, what if you have multiple plots and you want them side by side for comparison? You can do so by using the `plt.subplot()` function.

```
fig, axes = plt.subplots(2, 1, figsize=(5, 10))
sns.scatterplot(data=stroke_data, x='age', y='bmi', alpha=0.6, ax=axes[0])
sns.scatterplot(data=stroke_data, x='age', y='avg_glucose_level', alpha=0.6, ax=axes[1])
plt.show()
```
The first argument `2` tells `plt.subplots()` how many rows you want to organize in the subplots, and the `1` means you want only 1 column. We used the `sns.scatterplot()` function twice to plot 2 figures, and the argument `ax=` to tell `seaborn` where to display the subplots exactly. The rest is the same as the single figures above.

If the figures have the same axis label and ticks, we can make them share the same ones to save space. And just like before, we can set the titles as well:

```
fig, axes = plt.subplots(2, 1, figsize=(5, 8), sharex=True)
sns.scatterplot(data=stroke_data, x='age', y='bmi', alpha=0.6, ax=axes[0])
axes[0].set_title('Scatter plot of BMI vs age')
sns.scatterplot(data=stroke_data, x='age', y='avg_glucose_level', alpha=0.6, ax=axes[1])
axes[1].set_title('Scatter plot of avg_glucose_level vs age')
plt.tight_layout()
plt.show()
```
As you can see, we added the argument `sharex=True` to the function `plt.subplots()` to tell Python the subplots are sharing the x-axis. We also added the optional `plt.tight_layout()` to reduce spacing between the plots and improve the overall aethestic.


## Seaborn and distribution visualization

If you think that the histogram is not enough to visualize the distribution, you might want to try box plot and violin plot. You can use the `seaborn` package for that. Using `seaborn` you can visualize another information in the figure by using color. 

### Box plot

We simply use the `sns.boxplot()` function to do the boxplot. 
```
sns.boxplot(data=stroke_data, x="heart_disease", y="bmi", hue="stroke", fill=False, gap=.1)
plt.title('Box Plot of BMI by Heart Disease and Stroke Status')
plt.show()
```
With the box plot, we can identify the outliers more easily. `fill=False` will tell `seaborn` not to fill solid color inside the boxes, `gagp=.1` is the gap between the boxes for each category of the x-axis.


### Violin plot

If you want to visualize the distributions another way, you might want to try violin plots. We will use `sns.violinplot()`.

```
sns.violinplot(data=stroke_data, x="heart_disease", y="bmi", hue="stroke", split=True, gap=.1, inner="quart")
plt.title('Violin plot of BMI by heart disease and stroke status')
plt.show()
```

If you use the argument `split=True`, only half of the violins will be plotted for easier comparison. `inner="quart"` means quantiles of the data will be shown inside the violins, you may also choose `inner="box"` to display box-and-whisker plot.


## Visualizing correlation


### Pairplot

We can plot pairwise scatterplots to try and see if there is any correlations that exist between any pair of variables. This is only a preliminary visualization, but it is a good place to start. We will use `seaborn` to help us. But first we need to subset the dataframe because there are some categorical variables. We will select all 3 numerical variables plus the 'stroke' column:

```
df_pairplot = stroke_data[['age', 'bmi', 'avg_glucose_level', 'stroke']]
```

Now, we can use the `sns.pairplot()` function to make the pairplot. We will color the datapoint according to the 'stroke' status.

```
sns.pairplot(
    df_pairplot,
    hue="stroke",      
    diag_kind="kde",      
    markers=["o", "s"], plot_kws={'s': 10}
)
plt.suptitle("Pairwise Relationships in stroke data", y =1.02)
plt.show()
```
The argument `hue="stroke"` tells `seaborn` which information it should use to color the data points. `diag_kind="kde"` will get you kernel density estimation (kde)`*` on the diagonal, `seaborn` also support other types such as histogram. `markers=["o","s"]` will specify what marker shapes you want. Finally, `plot_kws={'s':10}` will set the size of the data point. `sns.pairplot()` returns a `PairGrid` object, that is to say the usual `matplotlib` function `plt.title()` will not work, so we use `plt.suptitle()` to add a title for all subplots at the top.  
If you want more details of the arguments of the function, please check the [seaborn](https://seaborn.pydata.org/index.html) documentation.

Once you have made the pairplot, you will notice that the data points of the '0's are being plotted on top of the '1's. We can solve this by reordering the dataframe like so:
```
df_pairplot_reordered = pd.concat([df_pairplot[df_pairplot['stroke'] == 0],df_pairplot[df_pairplot['stroke'] == 1]]).reset_index(drop=True)
```
We are subsetting the dataframe into 2, rows with '0's in the 'stroke' column and '1's, then we are merging them together putting '0's first. This way when `seaborn` make the plots, it will display rows with '1's last, thus they will be on top. `reset_index(drop=True)` will get rid of the old index, instead python will assign clean integer index to the dataframe. 

Now we can make the pairplot again:
```
sns.pairplot(
    df_pairplot_reordered,
    hue="stroke",      
    diag_kind="kde",      
    markers=["o", "s"],plot_kws={'s': 10}
)
plt.suptitle("Pairwise Relationships in stroke data", y =1.02)
plt.show()
```
Now the figure looks slightly better.

`*` KDE is a non-parametric algorithm that will estimate the shape of the density of the data. [KDE](https://arxiv.org/abs/1704.03924#)


### Heatmap

If we want a bit more details on their relationships, we can try getting the Pearson correlation. Since we only have 3 columns that are numerical in nature, we will exclude the other columns first by typing:

```
stroke_numerical = stroke_data.select_dtypes(include=['float64'])
```
We are selecting columns that with the data type being a 'float', which is a real number with a decimal point. The other columns contain categorical data represented as an 'object' or 'int64', so we will exclude them. We use the function that comes with a `pandas` dataframe object `select_dtypes()` to select only `float64`.

Next, we will use another `pandas` dataframe object function `corr()`. It will compute the pairwise correlation between the the columns that are in the dataframe. If you want more information about `corr()`, please visit the [Pandas](https://pandas.pydata.org/docs/index.html). We will leave every argument as default and get the pearson correlations:

```
correlations_df = stroke_numerical.corr()
```
We will now visualize the results using a heatmap. This can easily be done with a few lines of code, we will again be using `seaborn` to help us.

```
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlations_df,
    annot=True,        # show correlation values in cells
    fmt=".2f",         # format to two decimal places
)
plt.title("Correlation matrix")
plt.show()
```

`annot=True` will display the Pearson values in the cells. `fmt=".2f"` will display the values in 2 decimal places. Please check the [Seaborn](https://seaborn.pydata.org/index.html) documentation for more details.




## Conclusion

In this tutorial, you have learned how to visualize data with the `matplotlib` and `seaborn` package. There are other packages available and maybe other ways to make the same figure, but at least now you know the basics. 



