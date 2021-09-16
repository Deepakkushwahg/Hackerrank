size=int(input())
lst=list(map(int, input().split()))
a=set()
b=set()
for i in lst:
    if(i not in a):
        a.add(i)
        b.add(i)
    else:
        b.discard(i)
c=b.pop()
print(c)
