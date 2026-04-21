import pandas as pd 

data ={
    "name":["aditay","khusahl","ratnesh","bhumi","gourav","rahul","astha","rhohit"],
    "age":[12,32,32,24,23,22,21,11],
    "sallery":[200,232,232,3232,4342,2424,242,234],
    "performance":[99,23,23,42,43,42,11,33]
}
df =pd. DataFrame(data)

print(df)

df["bouns"] = df["sallery"] *10

print(df)

# using inset method 
# jab ham isnsert mathod usee karte he toh ham jaha cahe wha column insert kar sakte he or vo start forward method thi jime last me hota tha column add

# df.insert(loc,"some name" , some data)

df.insert(0," emoployee id ",[10,121,12,121,1212,112,112,122])
print(df)

