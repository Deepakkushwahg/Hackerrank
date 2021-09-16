n=int(input())
sm=0
st=input()
s=st.split()
x=s.index('MARKS')
for i in range(n):
    lst=list(input().split())
    sm+=int(lst[x])
avg=sm/n
print("{:.2f}".format(avg))
