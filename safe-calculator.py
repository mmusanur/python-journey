num1 = float(input("enter your first number :"))
num2 = float(input("enter your second number :"))

print("Addition", num1 + num2)
print("Subtraction", num1 - num2)
print("Multiplication", num1 * num2)

if(num2!=0):
    print("Division", num2 / num1)
else:
    print("cannot divide by zero")