import pandas as pd 

data ={
    "name":["aditay","khusahl","ratnesh","bhumi","gourav","rahul","astha","rhohit"],
    "age":[12,32,32,24,23,22,21,11],
    "sallery":[200,232,232,3232,4342,2424,242,234],
    "performance":[99,23,23,42,43,42,11,33]
}
df = pd.DataFrame(data)


print("sample data farme")

print(df)
print("districtive statistics")
print(df.describe())

