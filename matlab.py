# import library
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#create a messy dataset
raw_data={
    "Customer_id":[1,2,3,4,5,6,7,8,9,10],
    "name":["Alice","Bob","Charlie","David","Eva","Frank","Grace","Hannah","Ian","Jack"],
    "age":[25,"Thirty",35,"",45,50,55,60,65,70],
    "Purchase_amount":[100,200,300,400,500,600,700,800,900,1000],
    "signed up_date":["2021-01-01","2021-02-01","2021-03-01","2021-04-01","","2021-06-01","2021-07-01","2021-08-01","2021-09-01","invalid_date"],
}
df=pd.DataFrame(raw_data)
print("----Messy Dataset----")
print(df)
print(df.dtypes)
print("----Cleaned Dataset----")
print(df.drop_duplicates())
print(df.duplicated().sum())
print(df.info())