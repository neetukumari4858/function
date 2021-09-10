def add(x,y):
        a=x+y
        return(a)
def sub(e,f):
        c=e-f
        return(c)
def multi(h,i):
        k=h*i
        return k
def divide(v,w):
        t=v//w
        return t
def exponemts(q,i):
        r=q**i
        return r
def main():
    op=input('enter operator')
    if op=="+":
        print(add(3,2))
    if op=='-':
        print(sub(5,6))
    if op=='*':
        print(multi(6,5))
    if op=="//":
        print(divide(2,4))
    if op=="**":
        print(exponemts(5,6))

main()