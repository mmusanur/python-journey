balance = 10000
withdrawal = int(input("Enter Your Ammount :"))

if withdrawal <= balance:
    print("Take taka")
    balance = balance - withdrawal
    print("Remaining Balance:", balance)
else:
    print("Insufficient Balance")    