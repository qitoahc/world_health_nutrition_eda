import pandas as pd 
import numpy as np 

wrldhlth = pd.read_csv('./data.csv')
print(wrldhlth.head())
print(wrldhlth.describe())

