'''. 🔗 Feature Engineering for ML
'''
import pandas as pd

df = pd.read_csv("ecommerce.csv")

# Create new features
df['Total_Spend'] = df['Quantity'] * df['UnitPrice']
df['Discounted_Price'] = df['Total_Spend'] * (1 - df['DiscountRate'])

# Binning continuous variable
df['Age_Group'] = pd.cut(df['CustomerAge'], bins=[0,18,35,50,70,100],
                         labels=['Teen','Young Adult','Adult','Middle Age','Senior'])

# Encode categorical
df = pd.get_dummies(df, columns=['Age_Group','Country'], drop_first=True)

print(df.head())