num=int(input("enter a number:-"))
i=0
a=[]
while i<=num:
    j=1
    b=[]
    while j<=i:
        b.append(j)
        j+=1
    a.append(b)
    i+=1
print(a)