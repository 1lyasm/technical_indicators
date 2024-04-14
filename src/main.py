import pandas as pd
import numpy as np
import pandas_ta as ta
from scipy.stats import linregress
df = pd.read_csv("data/data.csv")
print(df.tail())
zeros = df[df["volume"] == 0].index
df.drop(zeros, inplace=True)
print(df.isna().sum())
df["ATR"] = df.ta.atr(length=20)
df["RSI"] = df.ta.rsi()
df["Average"] = df.ta.midprice(length=1)
df["MA40"] = df.ta.sma(length=40)
df["MA80"] = df.ta.sma(length=80)
df["MA160"] = df.ta.sma(length=160)

def get_slope(arr):
    y = np.array(arr)
    x = np.arange(len(y))
    slope, intercept, rval, pval, stderr = linregress(x, y)
    return slope

