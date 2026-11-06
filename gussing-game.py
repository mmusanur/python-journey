secret_number= 7
while True:
    number = int(input("Enter your number"))
    if secret_number==number:
        print("your number is right")
        break
    elif secret_number > number:
        print("your number is too low")
    else:
        print("your number is bigger")    