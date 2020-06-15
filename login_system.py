users = {}


def logininfo():
    a = input("Have you registered yourself? (yes/No)  : ")
    print(a)
    if a == 'No':
        username = input("Enter your username : ")
        if username in users:
            print("Username already exists")
        else:
            password = input("Enter your password : ")
            users[username]=password
            print("You have successfully registered yourself ")


    elif a == 'yes':
        username = input("Enter your username : ")
        password = input("Enter your password : ")
        if users[username] == password:
            print("Logged in !")


def leave():
    b=""
    while b!= 'yes':
        logininfo()
        b = input("Do you want to quit? (yes/No) : ")
        if b=='yes':
            print("You have asked to quit")
        else:
            print("Please continue loggin!")


logininfo()
leave()



    