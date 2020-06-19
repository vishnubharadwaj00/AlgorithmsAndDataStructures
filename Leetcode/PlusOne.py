digits=[9,9,9]
def plusone(digits):
    n=len(digits)
    num=0
    for i in range(0,n):
        num+=digits[i]*pow(10,n-i-1)
        print(num)
    num+=1
    output=[int(d) for d in str(num)]
    return output

x=plusone(digits)
print(x)