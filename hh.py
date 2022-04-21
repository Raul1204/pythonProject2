import pandas as pd
import openpyxl as xl
import os
import matplotlib as plt

df = pd.read_csv('dataworld.csv', index_col="Countries")
df = df.drop(["Numbers"], axis=1)
df1 = df['Confirmed_2020'].nlargest(n=10)


print(df1)
