import pandas as pd

df = pd.read_csv('dirtydata3.csv')

print(df.duplicated())