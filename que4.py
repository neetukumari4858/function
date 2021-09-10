def add_number(x,y):
    sum=x+y
    return sum
num1=int(input('enter first no'))
num2=int(input('enter second no'))
print(add_number(num1,num2))
def add_number_list1(l1,l2):
    i=0
    p=[]
    while i<len(l1):
        k=add_number(l1[i],l2[i])
        i=i+1
        p.append(k)
    return p
print(add_number_list1([50,60,10],[10,20,13]))

