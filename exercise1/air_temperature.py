import pandas as pd

df = pd.read_csv("./air_temperature.csv")['Air temperature (degC)']
min = df.min()
max = df.max()
avg = df.mean()
std = df.std()

print(min, max, avg, std)
