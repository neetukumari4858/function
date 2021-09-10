def perfect(num):
    i=1
    while i<num:
        sum=0
        j=1
        while j<i:
            if i%j==0:
                sum=sum+j
            j=j+1
        if sum==i:
            print(i,"perfect no")
        i=i+1
perfect(1000)
def perfect1(var):
    sum1=0
    k=1
    while k<var:
        if var%k==0:
            sum1=sum1+1 
        k=k+1
    if sum1==var:
        print(var,"perfect no")
    else:
        print(var,"not perfect no")
        return perfect
num1=int(input("enter no"))
perfect1(num1)