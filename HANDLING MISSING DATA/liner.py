import pandas as pd

data = {
    "time":[10,20,30,40,50],
    "value":[100,None,300,None,500]
}
df=pd.DataFrame(data)
print("before interploeation")
print(df)

df["value"]=df["value"].interpolate(method="linear")
print("After interploeation")
print(df)

