import pandas as pd
import numpy as np
# get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\Users\Vineeth\OneDrive\Documents\CSE 160\crime_dataset.csv", low_memory = False)
a = df["Year" == 1980]
print a
