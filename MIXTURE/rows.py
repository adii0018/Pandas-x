import pandas as pd

asr =pd.read_json("sample_Data.json")

print("starting first 5 rows")
print(asr.head(5))

print("starting last 5 rows")
print(asr.tail(5))