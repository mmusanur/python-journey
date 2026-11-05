user_message = input("Enter your message: ").lower().strip()
if "available" in user_message:
    print("Yes sir, this product is available")
elif "price" in user_message:
    print("Sir, regular price is 5000 taka but discount now price is 3000 taka")
elif "delivery" in user_message:
    print("It takes 2 days")
elif "need" in user_message:
    print("Please give me your information")
elif "thank" in user_message:
    print("You are welcome")
else:
    print("Sorry, I don not understand")                  