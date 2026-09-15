import pandas as pd 

data = {
    "Name":["Arjun","Rahul","Anu","Meena"],
    "Age":[20,21,19,22]
    "Marks":[85,90,78,92]
}
df=pd.DataFrame(data)
print("Names:")
print(df["Name"])

print("\nMarks:")
print(df["Marks"])