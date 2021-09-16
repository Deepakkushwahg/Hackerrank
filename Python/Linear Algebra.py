import numpy as npy
n=int(input())
lst=[]
for i in range(n):
    ls=list(map(float, input().split()))
    lst.append(ls)
arr=npy.array(lst)
det=npy.linalg.det(arr)
d=str(det)
if(d[2]=='0'):
    print(det)
else:
    print("{:.2f}".format(det))
