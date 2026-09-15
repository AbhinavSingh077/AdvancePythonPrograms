import pandas as pd 

marks=pd.DataFrame({"ID":[1,2,3],"Marks":[78,85,92]})
students=pd.DataFrame({"ID":[1,2,3],"Name":["Amit","Ravi","Neha"]})

result=pd.merge(marks,students,on="ID")
print(result)
