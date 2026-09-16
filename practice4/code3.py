import pandas as pd 
import matplotlib.pyplot as plt

data = {"Name": ["Arun","Rahul","Anu","Meena","Vijay"], 
        "Marks": [85, 90, 78, 92, 88]
        }
df = pd.DataFrame(data)
df.plot(x="Name", y="Marks", kind="line")

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()