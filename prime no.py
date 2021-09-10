def prime(num):
    i=1
    while i<=100:
        j=1
        f=0
        while j<=i:
            if i%j==0:
                f=f+1
            j=j+1
        if f==2:
            print(' prime no' ,i)
        i=i+1
        if i==100:
            break
prime(100)
def prime1(num1):
  
    k=1
    fe=0
    while k<=num1:
        if num1%k==0:
            fe=fe+1
        k=k+1

    if fe==2:
        print(num1,"prime no")
    else:
        print(num1,"not prime no")
        return prime
x=int(input('enter no'))
prime1(x)