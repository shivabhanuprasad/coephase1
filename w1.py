while True:
    password = input("Enter a password: ")

    length = len(password) >= 8
    digit = any(char.isdigit() for char in password)
    upcase = any(char.isupper() for char in password)

    if length and digit and upcase:
        print("Strong password")
        break  
    else:
        print("Password must be at least 8 characters, contains least one digit,one uppercase letter")
