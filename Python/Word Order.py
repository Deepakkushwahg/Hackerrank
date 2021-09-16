from collections import Counter
n=int(input())
lst=[]
for i in range(n):
    word=input()
    lst.append(word)
st=set(lst.copy())
print(len(st))
z=Counter(lst)
ls=list(z.values())
for i in ls:
    print(i,end=' ')
