import pandas as pd 

data ={
    "name":["aditay","khusahl","ratnesh","bhumi","gourav","rahul","astha","rhohit"],
    "age":[12,32,32,24,23,22,21,11],
    "sallery":[200,232,232,3232,4342,2424,242,234],
    "performance":[99,23,23,42,43,42,11,33]
}
df =pd. DataFrame(data)

hii_sallery =df[df["sallery"]>1000]

print("employee jiknki sallery 1000 se jada hee")
print(hii_sallery)

# filtering row jisme doo condition lagegi 

filterr =df[(df["sallery"]>1000) & (df["age"] <30)]


print(filterr)

# using or condition 

hey =df[(df["sallery"]>9999900) | (df["age"] <80)]
