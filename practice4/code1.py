import pandas as pd 

data={"Name":["Amit","Ravi","Neha"],"Marks":[78,None,92]}
df=pd.DataFrame(data)

print(df.isnull())
print(df.dropna())
print(df.fillna(0))
