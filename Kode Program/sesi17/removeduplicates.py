import pandas as pd

df = pd.read_csv('dirtydata4.csv')

df.drop_duplicates(inplace = True)

print(df.to_string())

#Notice that row 12 has been removed from the result

