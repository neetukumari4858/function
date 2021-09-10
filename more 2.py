num_of_student=int(input("enter the  no of student"))
exp=int(input("enter exp of one student"))
def num():
    month_exp=num_of_student*exp
    if month_exp<=50000:
        print(month_exp,"badget ke ander hai")
    else:
        print(month_exp,"badget ke ander nhi hai")
num()