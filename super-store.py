import pandas as pd

df = pd.read_csv(
    'C:\\Users\\Avinash\\Desktop\\DCult\\excersise\\Super_store_purchase.csv')

#    Who are the frequent male/female customer (city wise)?7
df = df.fillna(0)
df['Total'] = df['Product_Category_1'] + \
    df['Product_Category_2'] + df['Product_Category_3']
cug = df.groupby(['City_Category', 'Gender', 'User_ID']).sum()
cug.loc[cug['Total'] > 4000.0].sort_values('Total', ascending=False)

# . Top 10 least interested products - gender and age group wise
df.groupby(['Product_ID']).count().sort_values('User_ID').head(10)

# From which city, males are shopping more?
df.groupby(['Gender', 'City_Category']).count()

# What are the products females are not interested?
a = df['Gender'] != 'F'
df['A'] = a
b = df[~df.Product_ID.isin([''])]
