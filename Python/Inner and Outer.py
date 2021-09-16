import numpy as np
array_A=np.array(list(map(int, input().split())))
array_B=np.array(list(map(int, input().split())))
print(np.inner(array_A,array_B))
print(np.outer(array_A,array_B))
