def check_number(n,m):
    if n%2==0 and m%2==0:
        return ("dono no even hai")
    else:
        return("not even no")
n=int(input("enter no"))
m=int(input("enter no"))
print(check_number(n,m))
def check_number_list(l1,l2):
    i=0
    while i<len(l1):
        if l1[i]%2==0 and l2[i]%2==0:
            print("even no")
        else:
            print("not even no")
        i=i+1
check_number_list([2, 6, 18, 10, 3, 75],[6, 19, 24, 12, 3, 87])
        


