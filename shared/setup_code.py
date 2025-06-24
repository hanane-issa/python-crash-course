import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'healthcare-dataset-stroke-data.csv'))
stroke_data = pd.read_csv(DATA_PATH)
