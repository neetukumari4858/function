
x=101
x_digit=list(str(x))
def harshed_no(x_digit):
    sum=0
    n=x_digit
    while (x_digit>0):
        rem=x_digit%10
        sum=sum+rem
        x_digit=x_digit//10
    if(n%sum==0):
        return("True  it is a harshed no")
    else:
        return("False it is not harshed")
l=harshed_no(int(x))
print(l)


