import numpy as npy
npy.set_printoptions(sign=' ')
lst=list(map(float, input().split()))
arr=npy.array(lst)
print(npy.floor(arr))
print(npy.ceil(arr))
print(npy.rint(arr))
        




