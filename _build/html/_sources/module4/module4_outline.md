# Outline for Pandas section (module 4) 

Toy dataset: 

1. Create your own Pandas dataframe from a dictionary 

2. Save a dataframe as csv or tab-delimited 

3. How to load a csv file 

4. How to load a tab-delimited file 

    a. Mention motivation: BED files are tab-delimited 

    b. Pd.read_csv(sep=“\t“) +skip first line when importing, column headers/rehsaping

    c. Specifying/removing header names, row numbers 

Stroke dataset: 

5. Load the stroke dataset 

6. Exploring and summarising data: 

    a. Df.describe() and df.info() (including checking column dtypes) 

    b. Df.agg() 

    c. Select rows and columns 

        i. iloc, loc; select one row, multiple rows 
        eg. stroke_data.avg_glucose_level to select a column 

        ii. select one column, several columns 

        iii. .values 

    d. Select rows/columns according to criteria 

        i. ~ in df for selection		 

        ii. .sum() to check the number of entries 

7. Join columns/rows in Pandas 

    a. Add a toy data column/row to the stroke dataset 

    b. Pd.concat vs pd.merge (also axis =0 vs 1) 

8. String manipulation: 

    a. Match „unknown“ to N/A: https://pandas.pydata.org/docs/user_guide/text.html 

    b. Regular expressions for filtering (e.g. str.contains, str.startswith, etc.) 

    c. Changing column names 

9. Handling missing data  

    a. How missing data are defined (https://pandas.pydata.org/docs/user_guide/missing_data.html)  

    b. Isnull 

    c. Filter according to isnull 

    d. Replace N/A with a mean (applied to one cell versus all rows or columns with lambda apply for example) 

 