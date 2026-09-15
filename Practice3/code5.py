import pandas as pd 

data = {
    "Name":["Arun","Rahul","Anu","Meena"],
    "Marks":[85,90,78,92]
}

df=pd.DataFrame(data)
df=df.sort_values("Marks",ascending=False)

print(df)