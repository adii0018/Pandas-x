import pandas as pd 

data ={
    "name":["aditay",None,"ratnesh","bhumi","gourav","rahul","astha","rhohit"],
    "age":[12,None,32,24,23,22,21,11],
    "sallery":[200,None,232,3232,4342,2424,242,234],
    "performance":[99,None,23,42,43,42,11,33]
}
df =pd. DataFrame(data)
print(df)

# isnull use karne pe agar true aaya toh value null he or agar false 

# .sum () last me lagaunag toh number batayega ki kitna null value he kisi column me 

print(df.isnull().sum())



