import pandas as pd

df = pd.read_csv('dirtydata2.csv')

df.fillna(130, inplace = True)

print(df.to_string())

#Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).

