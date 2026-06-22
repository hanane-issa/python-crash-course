import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

URL = "https://raw.githubusercontent.com/hanane-issa/python-crash-course/main/data/healthcare-dataset-stroke-data.csv"

stroke_data = pd.read_csv(URL)

url = "https://raw.githubusercontent.com/hanane-issa/python-crash-course/main/data/healthcare-dataset-stroke-data.csv"

try:
    stroke_data = pd.read_csv("../data/healthcare-dataset-stroke-data.csv")
except FileNotFoundError:
    stroke_data = pd.read_csv(url)