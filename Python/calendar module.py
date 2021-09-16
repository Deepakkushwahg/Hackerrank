import calendar
date=list(map(int, input().split(' ')))
d=calendar.weekday(date[2],date[0],date[1])
day=calendar.day_name[d]
for i in day:
    if(i.islower()):
        print(i.upper(),end='')
    elif(i.isupper()):
        print(i,end='')
        

    
