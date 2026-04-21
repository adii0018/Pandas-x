import pandas as pd

data={
    "name":["adii","khushal","rahul"],
    "age":["30","22","12"],
    "city":["jaypur","indore","bhopal"]
}
# yaha haam dat ko frame kar rahe he pd.data frame or uske andar distnory pass kar di 
df=pd.DataFrame(data)
print(df)
# aab agar dat ako sav ekarna ho toh yeeh use karnge csv formate me 
# or agar aapko indexing nhi chiye jase ki 0 1 2 toh aap index=false kar do 
'''df.to_csv("new data.csv",index=False)'''
'''df.to_excel("new data.xlsx",index=False)'''
df.to_json("new data.json")