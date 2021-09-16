lst1=list(map(int, input().split()))
setA=set(lst1)
n=int(input())
c=0
for i in range(n):
    lst=list(map(int, input().split()))
    st=set(lst)
    z=setA.issuperset(st)
    if(z):
        c+=1
if(c==n):
    print("True")
else:
    print("False")
