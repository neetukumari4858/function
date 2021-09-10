def function(list1,list2):
    list1.extend(list2)
    i=0
    k=[]
    while i<len(list1):
        if list1[i] not in k:
            k.append(list1[i])
        i=i+1
    k.sort()
    print(k)
function([1, 5, 10, 12, 16, 20],[1, 2, 10, 13, 16])




