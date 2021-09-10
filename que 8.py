n=int(input("enter no"))
def sqr(n):
    i=1
    dic={}
    while i<=n:
        dic[i]=i**2
        i=i+1
    print(dic)
sqr(n)