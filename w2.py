#login system with 3 chances
cuser= "shiva"
cpassword = "1030"
chances = 3

while chances > 0:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == cuser and password == cpassword:
        print("Login successful.")
        break
    else:
        chances -= 1
        print(f"Incorrect credentials. Attempts left: {chances}\n")

if chances == 0:
    print("Account locked.")
