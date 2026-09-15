import pandas as pd 
data = {
    "Name":["Arun","Rahul","Anu","Meena"],
    "Marks":[85,90,78,92]
}

df = pd.DataFrame(data)

df["Grade"]=["A","A+","B","A+"]

print(df)