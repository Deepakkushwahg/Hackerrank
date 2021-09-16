n, m=map(int, input().split())
x=[]
y=[]
for i in range(n):
    group_A=input()
    x.append(group_A)
for i in range(m):
    group_B=input()
    y.append(group_B)
for i in range(len(y)):
    if(y[i] in x):
        for j in range(len(x)):
            if(y[i]==x[j]):
                print(j+1,end=' ')
        print()
    else:
        print(-1)
