import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import sklearn

dataframe = pd.read_csv("elnino.csv")
dataframe.replace('.', np.nan, inplace=True)
print(dataframe.count())