def list(): 
    string_list = ["Rishabh", "Rishabh", "Abhishek", "Rishabh", "Divyashish", "Divyashish"]
    k=[]
    i=0
    while i<len(string_list):
        if string_list[i] not in k:
            k.append(string_list[i])
        i=i+1
    return (k)
l=list()
print(l)