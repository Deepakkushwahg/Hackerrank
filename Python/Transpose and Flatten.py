import numpy as np
r, c=map(int, input().split())
lst=[]
for i in range(r):
    ls=list(map(int, input().split()))
    lst.append(ls)
arr=np.array(lst)
print(arr.transpose())
print(arr.flatten())
