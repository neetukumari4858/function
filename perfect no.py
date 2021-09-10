def perfect():
    sum=0
    p=1
    i=1
    while i<1000:
        if p%i==0:
            sum=sum+i
        i=i+1
    if sum==p:
        print(p,"perfect no")
    else:
        print( p,"not perfect no")
    p=p+1
#num=int(input("enter any no:-"))
perfect()