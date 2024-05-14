import pandas as pd

df = pd.read_excel('loginData.xlsx')
numfila = df[df["Codigo"] == 23200082]
print(numfila["Nombre"].iloc[0])
print(df[df["Codigo"] == 23200082]["Nombre"].iloc[0])