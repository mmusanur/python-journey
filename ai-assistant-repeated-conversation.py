while True:
    message = input("You: ").lower()
    if "hello" in message:
        print("AI: Hello sir how can i help  you?")
    elif "shirt" in message:
        print("AI: Yes sir our shirt product is available now")
    elif "need" in message:
        print("AI: Yes sir this product also available")
    elif "price" in message:
        print("AI: Sir this product price is 500Taka")
    elif "delivary" in message:
        print("AI: Sir it takes 2 days only")
    elif "confirmd" in message:
        print("AI: Okay Sir!")
    elif "thank" in message:
        print("AI: You are welcome")
    else:
        print("AI: Sorry i do not understand! Do you want any product?")





