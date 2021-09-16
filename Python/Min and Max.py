import numpy as npy
r, c=map(int, input().split())
lst=[]
for i in range(r):
    ls=list(map(int, input().split()))
    lst.append(ls)
arr=npy.array(lst)
arry=npy.min(arr, axis=1)
print(max(arry))
