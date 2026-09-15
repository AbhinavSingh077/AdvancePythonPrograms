import pandas as pd 

data = {
    "Name":["Arjun","Rahul","Anu","Meena"],
    "Marks":[85,90,78,92]
}
df = pd.DataFrame(data)

print("maximum Marks:",df["Marks"].max())
print("Minimum Marks:",df["Marks"].min())