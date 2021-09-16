import numpy as npy
n=int(input())
lst1=[]
lst2=[]
for i in range(n):
    ls=list(map(int, input().split()))
    lst1.append(ls)
for i in range(n):
    ls=list(map(int, input().split()))
    lst2.append(ls)
arr1=npy.array(lst1)
arr2=npy.array(lst2)
print(npy.dot(arr1,arr2))
    
    
