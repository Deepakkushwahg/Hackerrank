from itertools import permutations
lst=input().split()
s=lst[0]
k=lst[1]
st=list(s)
st.sort()
perm=list(permutations(st,int(k)))
for i in perm:
    print("".join(list(i)))
