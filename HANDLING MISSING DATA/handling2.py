'''df.fillna(0, inplace=True) ka matlab hai ki agar tumhare DataFrame (df) me NaN (missing values) hain, to unhe 0 se replace kar diya jayega.
👉 Breakdown:
- fillna(0) → NaN values ko 0 se replace karega.
- inplace=True → Changes directly df par apply honge, naya DataFrame return nahi hoga.

'''
import pandas as pd 

data = {
    "name": [
        "aditay","None","ratnesh","bhumi","gourav","rahul","astha","rhohit",
        "neha","priya","arjun","sahil","meena","vikas","nisha","deepak",
        "komal","manish","pankaj","anjali"
    ],
    "age": [
        12,None,32,24,23,22,21,11,
        25,27,29,31,19,34,28,26,
        30,33,35,20
    ],
    "sallery": [
        200,None,232,3232,4342,2424,242,234,
        1200,1500,1800,2100,2500,2700,3000,3200,
        3500,3700,4000,4200
    ],
    "performance": [
        99,None,23,42,43,42,11,33,
        55,60,65,70,75,80,85,90,
        95,50,40,30
    ]
}

df=pd.DataFrame(data)

# df.fillna(0,inplace=True)
# print(df)


df["age"].fillna(df['age'].mean(),inplace=True)
df["sallery"].fillna(df['sallery'].mean(),inplace=True)
print(df)
