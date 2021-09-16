import numpy as npy
n, m, p=map(int, input().split())
lst=[]
for i in range(n):
    ls=list(map(int, input().split()))
    lst.append(ls)
for i in range(m):
    ls=list(map(int, input().split()))
    lst.append(ls)
arr1=npy.array(lst)
print(arr1)
