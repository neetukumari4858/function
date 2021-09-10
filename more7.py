def num(list1,list2):
    i=0
    k=[]
    while i<len(list1):
        if list1[i] in list2:
            k.append(list1[i])
        i=i+1
    return(k)
l=num([1, 342, 75, 23, 98],[75, 23, 98, 12, 78, 10, 1])
print(l)