def function(string_list):
    i=0
    k=[]
    while i<len(string_list):
        if string_list[i] not in k:
            k.append(string_list[i])
        i=i+1
    return(k)
l=function(["Delhi", "Delhi", "Mumbai", "Mumbai", "Delhi", "Chennai", 'Chennai'])
print(l)