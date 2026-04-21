import pandas as pd 

asr =pd.read_json("sample_Data.json")

print("displaying the info of data")

print(asr.info())

hy = pd.read_csv("sales_data_sample.csv")
print(hy.info())
