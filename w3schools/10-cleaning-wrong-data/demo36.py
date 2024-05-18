# W3Schools, Pandas Cleaning Wrong Data
import pandas as pd

df = pd.read_csv('data.csv')

for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True) # Remove row

print(df.to_string())