s=input()
j=0
k=0
l=0
m=0
n=0
for i in range(len(s)):
    if(s[i].isalnum()):
        j=1
    if(s[i].isalpha()):
        k=1
    if(s[i].isdigit()):
        l=1  
    if(s[i].islower()):
        m=1
    if(s[i].isupper()):
        n=1
if(j==1):
    print("True")
else:
    print("False")
if(k==1):
    print("True")
else:
    print("False")
if(l==1):
    print("True")
else:
    print("False")
if(m==1):
    print("True")
else:
    print("False")  
if(n==1):
    print("True")
else:
    print("False")
