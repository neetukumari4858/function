def greater_no():
    a=int(input("enter first no"))
    b=int(input("enter sec no"))
    c=int(input("enter third no"))
    if a>b and a>c:
        print(a,"a is greater no")
    elif b>a and b>c:
        print(b,"b is greater no")
    else:
        print(c,"c is greater no")
greater_no()