
def wrap(string, max_width):
    lst=list(string)
    l=2
    lst.insert(max_width,'\n')
    for i in range(len(lst)):
        lst.insert(l*max_width+l-1,'\n')
        l+=1
    string="".join(lst)
    return string

