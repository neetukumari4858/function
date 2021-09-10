def max_no(marks):
    i=0
    while i<len(marks):
        max=0
        j=0
        while j<len(marks[i]):
            x=marks[i][j]
            if x>max:
                max=x
            j=j+1
        print(max)
        i=i+1
max_no([[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76],[87,55.98,99]])
