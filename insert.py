age=int(input("enter the age"))
def eligible_for_vote():
    if age >=18:
        print("you are eligible")
    else:
        print("not eligible")
eligible_for_vote()