'''pd.merge(df1,df2, on ="column_name", how="type of join")'''


import pandas as pd 

#customer data frame 
df_customer= pd.DataFrame(
    {
        'customerid':[1,2,3,4],
        'name':["rahul","adii","khhusal","bhaiyuuu"]
        
    }
)

#order data frame 
df_order=pd.DataFrame(
    {
        'customerid':[1,2,3,5],
        'orderamount':[250,430,350,378]
        
    
    }
)

# merge 
df_merged =pd.merge(df_customer,df_order,on="customerid",how="right")

#print("inner join")
'''   customerid     name  orderamount
0           1    rahul          250
1           2     adii          430
2           3  khhusal          350
'''
#print("outer join")
'''   customerid      name  orderamount
0           1     rahul        250.0
1           2      adii        430.0
2           3   khhusal        350.0
3           4  bhaiyuuu          NaN
4           5       NaN        378.0
'''
#print("left join ")
'''   customerid      name  orderamount
0           1     rahul        250.0
1           2      adii        430.0
2           3   khhusal        350.0
3           4  bhaiyuuu          NaN
'''
#print("right join")
'''   customerid     name  orderamount
0           1    rahul          250
1           2     adii          430
2           3  khhusal          350
3           5      NaN          378
'''
print(df_merged)
