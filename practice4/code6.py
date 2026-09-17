import numpy as np

a=np.array([1,2,3,4,5,6])

parts=np.array_split(a, 3)
print(parts)