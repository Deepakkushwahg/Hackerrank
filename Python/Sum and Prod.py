import numpy as npy
r, c=map(int, input().split())
lst=[]
for i in range(r):
    ls=list(map(int, input().split()))
    lst.append(ls)
arr=npy.array(lst)
arry=npy.sum(arr, axis=0)
print(npy.product(arry))
