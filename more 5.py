def num(y):
    factorial=1
    while y>0:
        factorial=factorial*y
        y=y-1
    return factorial,"factorial"
i=int(input("enter any no"))
x=num(i)
print(x)
