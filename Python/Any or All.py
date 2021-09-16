n=int(input())
lst=list(map(int, input().split()))
f=c=0
for i in lst:
    if(i>0):
        c+=1
    r=0
    s=i
    while(i>0):
        x=i%10
        r=r*10+x
        i=i//10
    if(s==r):
        f=1
if(f==1 and len(lst)==c):
    print(all(lst))
else:
    print("False")
