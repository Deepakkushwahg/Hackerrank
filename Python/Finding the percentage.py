n=int(input())
marks=[]
for i in range(0,n):
    ls=list(input().split(' '))
    marks.append(ls)
    ls.clear
student=input()

s=0
c=0
for i in marks:
    for j in i:
        if(j==student):
            for k in range(0,len(i)-1):
                    s=s+float(i[k+1])
                    c=c+1
print("{:.2f}".format(s/c))
