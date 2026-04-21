import pandas as pd
# read data form csv file into data frame 
# ap = pd.read_csv("sales_data_sample.csv",encoding="latin1")

ap=pd.read_json("sample_Data.json")
print(ap)
