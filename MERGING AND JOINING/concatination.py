'''
vertically (rows-wise)
horizontally (cloumns wise)
pd.concate([df1,df2],axis=0,ignor_index=true)
'''
import pandas as pd 

#region 1
df_regoin1=pd.DataFrame({
    'cid':[1,2],
    "name":["adii","rahul"]
    
})
#regoin 2
df_regoin2=pd.DataFrame({
    'cid':[3,4],
    "name":["shyam","baba"]
})

#concatination vertically

df_concat =pd.concat([df_regoin1,df_regoin2],axis=0,ignore_index=True)
print(df_concat)
