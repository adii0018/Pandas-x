'''
1. how big is your data set
2. what are name of the columns
shape and columns 
'''

import pandas as pd 

data ={
    "name":["aditay","khusahl","ratnesh","bhumi","gourav","rahul","astha","rhohit"],
    "age":[12,32,32,24,23,22,21,11],
    "sallery":[200,232,232,3232,4342,2424,242,234],
    "performance":[99,23,23,42,43,42,11,33]
}

df = pd. DataFrame(data)

print(df)
print(f"shape: {df.shape}")
print(f"column name: {df.columns}")
