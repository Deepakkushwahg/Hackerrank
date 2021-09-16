import numpy as npy
r, c=map(int, input().split())
lst1=[]
lst2=[]
for i in range(r):
    ls1=list(map(int, input().split()))
    lst1.append(ls1)
for i in range(r):
    ls2=list(map(int, input().split()))
    lst2.append(ls2)
arr1=npy.array(lst1)
arr2=npy.array(lst2)
print(npy.add(arr1,arr2))
print(npy.subtract(arr1,arr2))
print(npy.multiply(arr1,arr2))
print(npy.floor_divide(arr1,arr2))
print(npy.mod(arr1,arr2))
print(npy.power(arr1,arr2))
