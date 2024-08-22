import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas.plotting import  scatter_matrix
import seaborn as sns


data = pd.read_excel('./data/2.elevator_failure_prediction.xlsx')

data.plot(kind='box',subplots=True, figsize=(12,13),layout=(3,3),sharex=False)
plt.savefig('./results/box.png')