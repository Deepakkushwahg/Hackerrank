def print_formatted(number):
    l=len(str(bin(number))[2:])
    for i in range(1,number+1):
        print(str(i).rjust(l,' '),oct(i)[2:].rjust(l,' '),hex(i).upper()[2:].rjust(l,' '),bin(i)[2:].rjust(l,' '))

