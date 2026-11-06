correct_password = "1234"
attempts = 2
while attempts > 0:
    password = input("Enter your password: ")
    if password==correct_password:
        print("Login successfull-Welcome")
        break
    else:
        attempts = attempts - 1
        print("Wrong password")
        print("Attempts left:", attempts)

    if attempts==0:
        print("Account Lock")