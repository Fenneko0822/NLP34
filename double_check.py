import pandas as pd

df = pd.read_csv("file.csv")
df_cleaned = df.dropna() 
df_cleaned.to_csv("cleaned_file.csv", index=False)
