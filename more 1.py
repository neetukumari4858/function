def num1(num):
    i=1
    while i<=num:
        if i%3==0:
            print(i,"nav")
        elif i %7==0:
            print(i,"gurukul")
        elif i%21==0:
            print(i,"navgurukul")
        i=i+1
num1(1000)