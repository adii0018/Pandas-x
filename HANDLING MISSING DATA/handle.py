# dropna()
#df.dropana(axis =1 ,inplace True)
import pandas as pd 

data ={
    "name":["aditay",None,"ratnesh","bhumi","gourav","rahul","astha","rhohit"],
    "age":[12,None,32,24,23,22,21,11],
    "sallery":[200,None,232,3232,4342,2424,242,234],
    "performance":[99,None,23,42,43,42,11,33]
}
df =pd. DataFrame(data)
print(df)

df.dropna(inplace=True)
print(df)

df.dropna(axis=1)
print(df)
