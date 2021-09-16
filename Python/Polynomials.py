import numpy as npy
p=npy.array(list(map(float, input().split())))
x=float(input())
print(npy.polyval(p,x))
