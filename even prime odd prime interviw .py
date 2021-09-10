def even(a):
    k=[]
    o=[]
    i=0
    while i<len(a):
        if a[i]%2==0:
            k.append(a[i])
        else:
            o.append(a[i])
        i=i+1
    print(k)
    print(o)
even([1,11,5,7,21,2,22,55])
def odd(x):
    w=[]
    j=0
    while j<len(x):
        l=1
        f=0
        while l<=x[j]:
            if x[j]%l==0:
                f=f+1
            l=l+1
        if f==2:
            w.append(x[j])
        else:
            w.append("   ")
        return w
print(odd([2,22]))
def prime(y):
    z=[]
    r=0
    while r<len(y):
        g=1
        f1=0
        while g<=y[r]:
            if y[r]%g==0:
                f1=f1+1
            g=g+1
        if f1==2:
            z.append(y[r])
        r=r+1
    return z
print(prime([1,11,5,7,21,55]))
    




  