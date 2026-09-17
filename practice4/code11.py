import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student Name": ["Arun", "Rahul", "Anu", "Meena", "Vijay"],
    "Marks": [85, 90, 78, 92, 88],
    "Subject": ["Python", "Java", "Python", "Data Science", "Java"]
}

df = pd.DataFrame(data)

print(df)


df.plot(
    x="Student Name",
    y="Marks",
    kind="bar",
    legend=False
)

plt.title("Student Marks")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.show()


subject_counts = df["Subject"].value_counts()

plt.pie(
    subject_counts.values,
    labels=subject_counts.index,
    autopct="%1.1f%%"
)

plt.title("Students by Subject")
plt.show()