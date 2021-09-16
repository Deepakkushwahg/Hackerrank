

def solve(s):
    st=s.capitalize()
    lst=list(st)
    for i in range(len(lst)):
        if(lst[i]==chr(32)):
            lst[i+1]=lst[i+1].upper()
    s="".join(lst)
    return s

