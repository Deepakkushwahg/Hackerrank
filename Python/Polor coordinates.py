from cmath import phase
from math import sqrt

z=complex(input())
x=z.real
y=z.imag
r=sqrt((x**2)+(y**2))
p=phase(complex(x,y))
print(r)
print(p)
