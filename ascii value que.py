def ascii(sex):
    d=sex.split()
    i=0
    while i<len(d):
        j=0
        while j<len(d[i]):
            print(ord(d[i][j]),end=" ")
            j=j+1
        i=i+1
ascii("my name is neetu")

        
