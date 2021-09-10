def strong_password():
    if "A" in password and "Z" in password and "2" in password and "8" in password and "$" in password:
        if len(password)>=6 and len(password)<=16:
            print("strong password")
    else:
        print(password,"wrong password")
password=input("enter a password")
strong_password()

