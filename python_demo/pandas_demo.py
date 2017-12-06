import pandas as pd
import numpy as np

names = ['WeiYen','Tom','Andrew','Perry']
s = pd.Series(names)
print(s)

dates = pd.date_range('20160101',periods=6) 
df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])

for i in range(0, 4):
    df.iloc[i, 1] = i

print(df)
print(df['b'])
print(df[df['b']>0])
df2 = pd.DataFrame({'A' : 1.,
                    'B' : pd.Timestamp('20130102'),
                    'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                    'D' : np.array([3] * 4,dtype='int32'),
                    'E' : pd.Categorical(["test","train","test","train"]),
                    'F' : 'foo'})
                    
print(df2)
print(df2.dtypes)
print(df2.index)
print(df2.columns)
print(df2.values)
df2.describe()
print(df2['C'])