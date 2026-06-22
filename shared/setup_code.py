import os

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
stroke_data = pd.read_csv("../data/healthcare-dataset-stroke-data.csv")

file_path = "../data/healthcare-dataset-stroke-data.csv"

if not os.path.exists(file_path):
    # Likely running in Colab or missing repo structure
    !wget -q https://raw.githubusercontent.com/hanane-issa/python-crash-course/main/data/healthcare-dataset-stroke-data.csv
    file_path = "healthcare-dataset-stroke-data.csv"

stroke_data = pd.read_csv(file_path)