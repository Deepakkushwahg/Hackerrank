x=int(input())
y=int(input())
z=int(input())
n=int(input())
m=[]
permutation=[]
for i in range(0,x+1):
    for j in range(0,y+1):
        for k in range(0,z+1):
            if((i+j+k)!=n):
                m.append(i)
                m.append(j)
                m.append(k)
                permutation.append(m)
                m=[]
print(permutation)
