from itertools import combinations
lst=input().split()
s=lst[0]
k=int(lst[1])
st=list(s)
st.sort()
for i in range(1,k+1):
    comb=list(combinations(st,i))
    for j in comb:
        print("".join(list(j)))
