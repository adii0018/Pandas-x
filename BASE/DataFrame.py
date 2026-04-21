'''🔥 1. DataFrame Create & Basic Info'''
#print(df)
#print(df.head())       # First 5 rows
#print(df.info())       # Data info
#print(df.describe())   # Stats

import pandas as pd 

data = {
    "name": [
        "aditay","khusahl","ratnesh","bhumi","gourav","rahul","astha","rhohit",
        "neha","priya","arjun","sahil","meena","vikas","nisha","deepak",
        "komal","manish","pankaj","anjali"
    ],
    "age": [
        12,32,32,24,23,22,21,11,
        25,27,29,31,19,34,28,26,
        30,33,35,20
    ],
    "sallery": [
        200,232,232,3232,4342,2424,242,234,
        1200,1500,1800,2100,2500,2700,3000,3200,
        3500,3700,4000,4200
    ],
    "performance": [
        99,23,23,42,43,42,11,33,
        55,60,65,70,75,80,85,90,
        95,50,40,30
    ]
}

df=pd.DataFrame(data)

print(df)


print(df.tail()) # last ke 5 
print(df.head()) # starting se 5 

print(df.info()) # deatils batat he size bhi 

print(df.describe())  # describe karan ho tab 