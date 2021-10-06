def reverse(x):
    if(x==0):
        return 0
    flag=0
    if(x<0):
        flag=1
        x=abs(x)
    lst = [int(i) for i in str(x)]
    lst.reverse()
    strings = [str(i) for i in lst]
    a_string = "".join(strings)
    an_integer = int(a_string)
    if flag==1:
        return -1*an_integer
    return an_integer

print(reverse(123))