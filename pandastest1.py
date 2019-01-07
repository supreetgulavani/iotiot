import pandas as pd
import numpy as np
index = pd.date_range('1/1/2000',periods=8)         #returns a fixed frequency date-time index
print(index)
long_series = pd.Series(np.random.randn(1000))      #created an 1-D array with random 1000 numbers
print(long_series.head(10))                         #prints the first n rows
print(long_series.tail(5))                          #prints the last n rows

d = {'one':pd.Series([1.,2.,3.,4.], index=['a','b','c','d']),'two':pd.Series([1.,2.,3.],index=['a','b','c'])}
df = pd.DataFrame(d)
print(df)
g = pd.DataFrame(d,index=['d','v','n'])
print(g)
p = pd.DataFrame(d,index=['a','b','d'],columns=['one','three'])
print(p) 
h = df.index
print(h)
l = df.columns
print(l)
